# import lxml
import requests
from bs4 import BeautifulSoup


def get_text_link(title):
    title_line = title.find(class_="titleline").find(name="a")
    title_text = title_line.getText()
    title_link = title_line.get("href")

    return title_text, title_link


def get_points(soup, id) -> int:
    points_span = soup.find(id=f"score_{id}")
    if points_span:
        points_str: str = points_span.getText()
        points_list = points_str.split()
        points = int(points_list[0])
    else:
        points = 0

    return points


def get_highest_article(articles: list):
    highest_points = articles[0]

    for article in articles:
        try:
            if article["points"] > highest_points["points"]:
                highest_points = article
        except TypeError:
            pass

    return highest_points


response = requests.get("https://news.ycombinator.com/news")
yc_website = response.text
soup = BeautifulSoup(yc_website, "html.parser")

titles = soup.find_all(class_="athing")
articles = []
for title in titles:
    id = title.get("id")
    article_text = get_text_link(title)
    article_points = get_points(soup, id)
    article = {"text": article_text, "points": article_points}
    articles.append(article)

best_article = get_highest_article(articles)

print(f"Title: {best_article["text"][0]}")
print(f"Link: {best_article["text"][1]}")
print(f"Points: {best_article["points"]} points")

# for title in titles:
#     article_text = title.find("a").getText()
#     article_link = title.find("a").get("href")
#     print(f"Article: {article_text} - link: {article_link}")

# *----------------------Learning----------------------#
# with open(r"website.html", "r") as file:
#     website = file.read()

# soup = BeautifulSoup(website, "html.parser")

# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)

# all_achor_tags = soup.find_all(name="a")
# for tag in all_achor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)

# company_url = soup.select_one(selector="p a")
# # print(company_url)

# name = soup.select(selector="#name")
# # print(name)

# headings = soup.select(".heading")
# print(headings)
