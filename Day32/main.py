# Day 32 | Automatic Birthday Wisher - Introducing smtplib and sending emails with Python

import smtplib
import pandas as pd
import datetime as dt
import random
from email.message import EmailMessage

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

today = dt.datetime.now()
current_month = today.month
current_day = today.day

birthday_data = pd.read_csv("birthdays.csv")
format_data = birthday_data.to_dict(orient="records")

for people in format_data:
    if people["month"] == current_month and people["day"] == current_day:
        letter = random.choice(letters)
        with open(letter) as file:
            default = file.read()
            email_body = default.replace("[NAME]", people["name"])

        my_email = "hlx.junkmail@gmail.com"
        password = "REDACTED"

        msg = EmailMessage()
        msg["Subject"] = "Happy Birthday!"
        msg["From"] = my_email
        msg["To"] = people["email"]
        msg.set_content(email_body)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=people["email"],
                                msg=msg.as_string()
            )
