from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField
from wtforms.validators import Required, Email

class LoginForm(Form):
    username = TextField('username', validators=[Required()])
    password = TextField('password', validators=[Required()])

class LunchForm(Form):
	title = TextField('title', validators=[Required()])
	post = TextField('post', validators=[Required()])

class SignupForm(Form):
    username = TextField('username', validators=[Required()])
    password = TextField('password', validators=[Required()])
    firstname = TextField('firstname', validators=[Required()])
    lastname = TextField('lastname', validators=[Required()])
    email = TextField('email', validators=[Required()])
    gender = TextField('gender', validators=[Required()])
    age = TextField('age', validators=[Required()])
    location = TextField('location', validators=[Required()])

class ReviewForm(Form):
    name = TextField('name', validators=[Required()])
    rate = TextField('rate', validators=[Required()])


