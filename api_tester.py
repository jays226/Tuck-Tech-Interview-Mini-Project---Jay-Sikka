import requests
import json

base_url = "http://127.0.0.1:5000"

def get():
    url = f"{base_url}/get"
    response = requests.get(url)
    return response.json()


def post(text):
    url = f"{base_url}/post"

    headers = {
        'Content-Type': 'application/json',
    }
    raw_body = {
        'text': text
    }

    response = requests.post(url, headers=headers, json=raw_body)
    return response.json()


get_data = get()
print(json.dumps(get_data, indent=4))

sentence = input("What sentence to add? ")

post_data = post(sentence)
print(json.dumps(post_data))

get_data = get()
print(json.dumps(get_data, indent=4))
