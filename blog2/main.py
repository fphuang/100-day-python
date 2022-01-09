import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
from wtforms.widgets import TextArea

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = TextAreaField("Blog Content", validators=[DataRequired()], render_kw={"rows": 20, "cols": 60})
    submit = SubmitField("Submit Post", )


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = BlogPost.query.all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    if request.method == 'GET':
        edit_form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body
        )
        return render_template('make-post.html', form=edit_form, post=post, is_edit=True)

    post.title = request.form['title']
    post.subtitle = request.form['subtitle']
    post.author = request.form['author']
    post.img_url = request.form['img_url']
    post.body = request.form['body']
    db.session.commit()
    return get_all_posts()


@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    form = CreatePostForm()
    if request.method == 'POST':
        post_new = BlogPost()
        post_new.title = form.title.data
        post_new.subtitle = form.subtitle.data
        post_new.date = date.today().strftime("%b %d, %Y")
        post_new.body = form.body.data
        post_new.author = form.author.data
        post_new.img_url = form.img_url.data
        db.session.add(post_new)
        db.session.commit()
        return get_all_posts()
    return render_template('make-post.html', form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/delete/<int:post_id>")
def delete(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return get_all_posts()


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
