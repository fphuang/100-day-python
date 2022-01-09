from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(label='Email Address',
                       validators=[DataRequired()])
    password = PasswordField(label='Password',
                             validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label='Log In')
