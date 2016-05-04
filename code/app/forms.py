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
    extraverted = TextField('extraverted', validators=[Required()])
    agreeable = TextField('agreeable', validators=[Required()])
    consc = TextField('consc', validators=[Required()])
    emotional = TextField('emotional', validators=[Required()])
    experiences = TextField('experiences', validators=[Required()])
    pleasureseeking = TextField('pleasureseeking', validators=[Required()])
    nostalgia = TextField('nostalgia', validators=[Required()])
    catharsis = TextField('catharsis', validators=[Required()])
    aggression = TextField('aggression', validators=[Required()])
    escapism = TextField('escapism', validators=[Required()])
    sensationseeking = TextField('sensationseeking', validators=[Required()])
    artistic = TextField('artistic', validators=[Required()])
    informationseeking = TextField('informationseeking', validators=[Required()])
    boredomavoidance = TextField('boredomavoidance', validators=[Required()])
    socialization = TextField('socialization', validators=[Required()])


class ReviewForm(Form):
    name = TextField('name', validators=[Required()])
    rate = TextField('rate', validators=[Required()])


class SearchForm(Form):
    name = TextField('name', validators=[Required()])

class WatchForm(Form):
    name = TextField('name', validators=[Required()])