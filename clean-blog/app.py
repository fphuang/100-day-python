from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)


def load_posts():
    response = requests.get(url='https://api.npoint.io/1c535ff2282c82cff720')
    response.raise_for_status()
    return response.json()


posts = load_posts()


@app.get('/')
def go_home():
    return render_template('index.html', posts=posts)


@app.get('/contact')
def go_to_contact():
    return render_template('contact.html')


@app.get('/about')
def go_to_about():
    return render_template('about.html')


@app.get('/post/<int:index>')
def show_post(index):
    for post in posts:
        if int(post["id"]) == index:
            return render_template('post.html', post=post)


@app.post('/contact')
def receive_data():
    send_email(data={
        "name": request.form["name"],
        "email": request.form["email"],
        "message": request.form["message"],
        "phone": request.form["phone"]})

    return render_template('contact.html', message_sent=True)


def send_email(data):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        message = format_message(data)
        print(message)
        connection.starttls()
        connection.login(user="huang.fp@gmail.com", password="******")
        connection.sendmail(from_addr=data["email"], to_addrs="huang.fp@gmail.com",
                            msg=f"Subject: from {data['name']}\n\n{message}")


def format_message(data):
    return f"<p>name: {data['name']}" \
           f"<p>email: {data['email']}" \
           f"<p>phone: {data['phone']}" \
           f"<p>message: {data['message']}"


if __name__ == '__main__':
    app.run(debug=True)
