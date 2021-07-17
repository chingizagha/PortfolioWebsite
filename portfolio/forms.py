from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 



class ContactForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=250)])
    submit = SubmitField('Send Message')