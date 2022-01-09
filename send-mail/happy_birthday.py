import datetime as dt
import smtplib
import random
import datetime as dt
import pandas as pd


def load_birthdays():
    df = pd.read_csv('birthdays.csv')
    return {(row["month"], row["day"]): row for (index, row) in df.iterrows()}


def send_mail(content):
    email_address = "huang.fp@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_address, password="Strongdeneber****")
        connection.sendmail(from_addr=email_address,
                            to_addrs="huang.fp@gmail.com",
                            msg="subject:Happy birthday\n\n" + content)


def happy_birthday():
    today = dt.datetime.now()
    today_tuple = (today.month, today.day)
    birth_dict = load_birthdays()
    if today_tuple in birth_dict:
        birthday_person = birth_dict[today_tuple]
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", birthday_person["name"])
            send_mail(content)


happy_birthday()
