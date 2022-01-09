import smtplib
import datetime as dt

def send_mail():
    email_address = "huang.fp@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_address, password="Strongdeneberxxxx")
        connection.sendmail(from_addr=email_address,
                            to_addrs="huang.fp@gmail.com",
                            msg="subject:Merry X'mas\n\nsent from python client. ")

import datetime as dt

