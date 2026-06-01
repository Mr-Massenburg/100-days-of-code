# Day 35 | Need Umbrella SMS - Use APIs that require authentication. Get weather data and send an SMS message if the forecast calls for rain. Introduced Environment Variables. 

import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("KEY_SID")
auth_token = os.environ.get("KEY_TOKEN")

MY_LAT = 41.8667
MY_LNG = -103.6672
API_KEY = os.environ.get("KEY_OWM")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", parameters)
response.raise_for_status()

data = response.json()

need_umbrella = False

forcast_codes = [day["weather"][0]["id"] for day in data["list"]]

for weather in forcast_codes:
    if weather < 700:
        need_umbrella = True
        break

if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. ☔️",
        from_="+15005550006", # twilio test number
        to="+11234567890", # dummy number
    )
    print(message.status)

