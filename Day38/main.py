# Day 38 | Workout Tracker - Code takes plan text input from user and feeds it into API to understand what the workout is and estimate data. Then pushes data to a Google Sheet using Sheety API

import os
from datetime import datetime
import requests

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")


BASE_API_URL = "https://app.100daysofpython.dev"
FIT_POST_URL = "/v1/nutrition/natural/exercise"

now = datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

fit_header = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

fit_params = {
    "query": input("Tell me which exercises you did: ")
}

fit_response = requests.post(f"{BASE_API_URL}{FIT_POST_URL}", json=fit_params, headers=fit_header)
fit_response.raise_for_status()
fit_data = fit_response.json()

exercise = fit_data["exercises"][0]["name"].title()
calories = fit_data["exercises"][0]["nf_calories"]
duration = fit_data["exercises"][0]["duration_min"]


add_row_params = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
sheety_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

add_row = "https://api.sheety.co/27c32f6966c58c00f49c62d078d585bb/workoutTracking/workouts"

add_row_response = requests.post(add_row, json=add_row_params, headers=sheety_header)
add_row_response.raise_for_status()



