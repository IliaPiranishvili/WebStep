from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields.simple import PasswordField, SubmitField


class Login(FlaskForm):
    username = StringField("სახელი")
    password = PasswordField("პაროლი")
    button = SubmitField("შესვლა")