# Day 37 | Pixela API Practice - ET, POST, PUT, and DELETE requests

import os
import requests
from datetime import datetime

username = "mrmassenburg"
token = os.environ.get("PASSWORD")
pixela_endpoint = "https://pixe.la/v1/users"

# Create a new user (POST request)

user_params = {
    "token": "asdf;lkjIJasdflkSAD",
    "username": "mrmassenburg",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_id = "graph1"

# Create a new graph (POST request)

graph_params = {
    "id":"graph1",
    "name": "Python Practice",
    "unit": "hour",
    "type": "float",
    "color": "kuro",
}
headers = {
    "X-USER-TOKEN": token
}
# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.today()
today.strftime("%Y%m%d")

yesterday = datetime(year=2026, month=6, day=4)
yesterday_date = yesterday.strftime("%Y%m%d")

post_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

# Post a pixel (POST request)

pixel_params = {
    "date": yesterday_date,
    "quantity": "3"
}

# response = requests.post(post_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{yesterday_date}"

# Update a pixel (PUT request)

update_params = {
    "quantity": "2.5"
}

# response = requests.put(update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{yesterday_date}"

# Delete a pixel (DELETE request)

response = requests.delete(delete_pixel_endpoint, headers=headers)
print(response.text)
