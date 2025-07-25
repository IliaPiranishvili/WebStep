from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, length, equal_to


class Register(FlaskForm):
    user = StringField("სახელი", validators=[DataRequired(), length(min=4)])
    birthday = DateField("დაბადების თარიღი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired(), length(min=8)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(),  equal_to("password")])
    submit = SubmitField("რეგისტრაცია")


class Post(FlaskForm):
    postname = StringField("პოსტის სახელი")
    discribe = StringField("პოსტის აღწერა")
    img = FileField()
    button =  SubmitField("გამოქვეყნება")
