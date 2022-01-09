from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    posts = Post().get_posts()
    return render_template("index.html", posts=posts)


@app.get('/post/<int:index>')
def read_post(index):
    posts = Post().get_posts()
    filtered = [post for post in posts if post["id"] == index]
    return render_template('post.html', post=filtered[0])


if __name__ == "__main__":
    app.run(debug=True)
