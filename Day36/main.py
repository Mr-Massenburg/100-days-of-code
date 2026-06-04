#Day 36 | Stock Movement Alerts - Automatically send sms with news alerts about the company if the stock price moves more than 5%

import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_KEY = os.environ.get("KEY_STOCK")
NEWS_KEY = os.environ.get("KEY_NEWS")

account_sid = os.environ.get("KEY_SID")
auth_token = os.environ.get("KEY_TOKEN")


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_KEY,
}

stock_response = requests.get("https://www.alphavantage.co/query", stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()
stock_data = [value for (key, value) in data["Time Series (Daily)"].items()]

yesterday_close = float(stock_data[0]["4. close"])
day_before_close = float(stock_data[1]["4. close"])

change = (yesterday_close - day_before_close) / yesterday_close
change_percent = change * 100

if change_percent <= -5 or change_percent >=5:
    news_parameters = {
        "q": COMPANY_NAME,
        "pageSize": 3,
        "apiKey": NEWS_KEY
    }

    new_response = requests.get("https://newsapi.org/v2/everything", news_parameters)
    new_response.raise_for_status()
    data = new_response.json()

    icon = ""

    if change_percent < 0:
        icon = "🔻"
    else:
        icon = "🔺"

    client = Client(account_sid, auth_token)

    for article in data["articles"]:
        msg = (f"{STOCK}: {icon}{abs(change_percent):.2f}%\n"
               f"Headline: {article["title"]}\n"
               f"Brief: {article["description"]}")

        message = client.messages.create(
            body=msg,
            from_="+15005550006",  # twilio test number
            to="+11234567890",  # dummy number
        )
        print(message.status)





