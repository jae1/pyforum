from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired('Subject is required.')])
    content = TextAreaField('Body', validators=[DataRequired('Body is required.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('Body', validators=[DataRequired('Body is required.')])

class NewUserForm(FlaskForm):
    email = EmailField('Email Address', [DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', 'Passwords do not match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])