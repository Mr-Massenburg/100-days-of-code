# Day 33 | Automated Email sent with ISS is above, and it's dark out - Started using API request to get data

import requests
from datetime import datetime, timezone
import smtplib
from email.message import EmailMessage
import time

MY_LAT = 37.540726
MY_LONG = -77.436050

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()

    iss_long = float(iss_data["iss_position"]["longitude"])
    iss_lat = float(iss_data["iss_position"]["latitude"])

    lat_close = False
    long_close = False

    if iss_lat <= MY_LAT + 5 and iss_lat >= MY_LAT - 5:
        lat_close = True
    if iss_long <= MY_LONG + 5 and iss_long >= MY_LONG - 5:
        long_close = True

    if lat_close and long_close:
        return True

    return False

def is_it_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_data = response.json()

    sunrise_hr = int(sun_data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset_hr = int(sun_data["results"]["sunset"].split('T')[1].split(':')[0])
    now = datetime.now(timezone.utc)
    if now.hour < sunrise_hr or now.hour > sunset_hr:
        return True

    return False

def send_email():
    my_email = "hlx.junkmail@gmail.com"
    password = "REDACTED"

    msg = EmailMessage()
    msg["Subject"] = "The ISS Is In View"
    msg["From"] = my_email
    msg["To"] = "marquismassenburg@yahoo.com"
    msg.set_content("Look Up!")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="marquismassenburg@yahoo.com",
                            msg=msg.as_string()
        )

while True:
    if is_it_dark() and is_iss_close():
        send_email()
    time.sleep(60)
