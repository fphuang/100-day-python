import datetime as dt
import smtplib
import random


def get_quote():
    with open('quotes.txt', 'r') as quotes_file:
        quotes = quotes_file.readlines()
        return random.choice(quotes)


def mail_quote(quote):
    email_address = "huang.fp@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_address, password="Strongdeneber2050")
        connection.sendmail(from_addr=email_address,
                            to_addrs="huang.fp@gmail.com",
                            msg="subject:Happy Week\n\n" + quote)


def send_reminder():
    now = dt.datetime.now()
    if now.weekday() == 2:
        quote = get_quote()
        mail_quote(quote)


send_reminder()
