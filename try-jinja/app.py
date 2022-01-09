from flask import Flask, render_template
import random
import datetime
import utils

app = Flask(__name__)


@app.get('/')
def home():
    rand_number = random.randint(1, 10)
    now = datetime.datetime.now()
    return render_template('index.html', num=rand_number, year=now.year)


@app.get('/guess/<path:name>')
def guess_age_and_gender(name):
    gender = utils.guess_gender(name)
    age = utils.guess_age(name)
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.get('/blog/<num>')
def get_blog(num):
    all_posts = utils.get_blog()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
