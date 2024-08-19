import requests


def get_quote():
    parameters = {"amount": 10, "type": "boolean"}
    try:
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching ISS data: {e}")
    else:
        data = response.json()

    return data["results"]


question_data = get_quote()
