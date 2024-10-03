import os
import smtplib as smtp

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

URL = "https://www.amazon.com.mx/dp/B09ZLV74XM/?coliid=ISADNR4976S3L&colid=7W1FE0DFP9RA&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it_im"
BUY_PRICE = 700

load_dotenv()

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,es-MX;q=0.8,es;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}


def get_html() -> BeautifulSoup:
    response = requests.get(URL, headers=header)
    fake_wbsite = response.text
    soup = BeautifulSoup(fake_wbsite, "html.parser")

    return soup


def get_price(soup: BeautifulSoup) -> float:
    price_list = soup.find(class_="aok-offscreen").get_text().split("$")  # type: ignore
    price_float = float(price_list[1])

    return price_float


def get_name(soup: BeautifulSoup) -> str:
    name = soup.find(id="productTitle").getText().split()  # type: ignore
    name_str = " ".join(name)

    return name_str


def send_email(my_email: str, python_mail_password: str, name: str, price: float):
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password=python_mail_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=(
                f"Subject:Lower Price Alert!\n\n" f"{name} is now ${str(price)}\n{URL}"
            ).encode("utf-8"),
        )
    print("email sent")


def main():
    my_email = os.environ["ULTRA_MAIL_MAIL"]
    python_mail_password = os.environ["ULTRA_MAIL_PASS"]
    soup = get_html()
    price = get_price(soup)
    name = get_name(soup)
    if price < BUY_PRICE:
        send_email(my_email, python_mail_password, name, price)


if __name__ == "__main__":
    main()
