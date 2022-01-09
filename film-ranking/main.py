from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import tmdb

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)

db.create_all()


def create_movie_sample():
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, "
                    "pinned down by an extortionist's sniper rifle. Unable to leave or "
                    "receive outside help, Stuart's negotiation with the caller leads "
                    "to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )

    db.session.add(new_movie)
    db.session.commit()


# create_movie_sample()

class UpdateRatingForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = TextAreaField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    edit_form = UpdateRatingForm()
    if request.method == 'POST':
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        db.session.commit()
        return home()

    return render_template('edit.html', form=edit_form, movie=movie)


@app.get("/delete/<int:movie_id>")
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    if movie_to_delete:
        db.session.delete(movie_to_delete)
        db.session.commit()

    return home()


@app.route('/add', methods=['GET','POST'])
def add():
    add_form = AddMovieForm()
    if request.method == 'POST':
        result = tmdb.search_movie(add_form.title.data)
        if result:
            movie = Movie()
            movie.title = result['title']
            movie.year = result['year']
            movie.description = result['description']
            movie.rating = result['rating']
            movie.review = result['review']
            movie.ranking = result['ranking']
            movie.img_url = result['img_url']

            db.session.add(movie)
            db.session.commit()
        return home()

    return render_template('add.html', form=add_form)


if __name__ == '__main__':
    app.run(debug=True)
