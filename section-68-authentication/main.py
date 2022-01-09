from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html", logged_in=current_user.is_authenticated)

    new_user = User()
    new_user.name = request.form.get("name")
    new_user.email = request.form.get("email")
    new_user.password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return redirect(url_for("secrets"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form.get("email").strip()
    user = User.query.filter_by(email=email).first()
    if not user:
        flash('This email does not exist. Please try again.')
        return render_template("login.html")

    password_entered = request.form.get("password")
    if not check_password_hash(user.password, password_entered):
        flash('Password incorrect. Please try again.')
        return render_template("login.html")

    login_user(user)
    return redirect(url_for("secrets"))


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user=current_user, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
