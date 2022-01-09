from flask import Flask, render_template, request


app = Flask(__name__)


@app.get('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def log_in():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>You have logged in as {name.title()}</h1>"


if __name__ == '__main__':
    app.run(debug=True)