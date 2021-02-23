from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Email, Length
from wtforms import validators, StringField, SubmitField, TextAreaField

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

