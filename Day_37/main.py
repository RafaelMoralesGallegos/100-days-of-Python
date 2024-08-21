import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "The Blood Wolf"

user_param = {
    "token": TOKEN,
    "username": "ultratumba",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_param)
print(response.text)
