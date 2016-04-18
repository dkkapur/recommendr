from flask import render_template, flash, redirect, request, session
from app import app
from .forms import LoginForm, LunchForm, SignupForm, ReviewForm
import pymongo, time

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
                           session=session)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		try:
			conn=pymongo.MongoClient()
			db = conn.nets
			userInfo = db.userInfo
			data = {}
			if (len(list(userInfo.find({'username' : request.form['username']}))) > 0):
				return redirect('/signup')
			data['username'] = request.form['username']
			data['password'] = request.form['password']
			data['firstname'] = request.form['firstname']
			data['lastname'] = request.form['lastname']
			data['email'] = request.form['email']
			data['gender'] = request.form['gender']
			data['age'] = request.form['age']
			data['location'] = request.form['location']
			data['reviews'] = {}
			userInfo.insert(data)
			return redirect('/index')

		except pymongo.errors.ConnectionFailure, e:
			print "Could not connect to MongoDB: %s" % e
			return redirect('/index')
	else:
		return render_template('signup.html', title='Sign Up', form=form, session = session)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		try:
			conn=pymongo.MongoClient()
			db = conn.nets
			userInfo = db.userInfo
			usernameToVerify = list(userInfo.find({'username': request.form['username']}))
			if(len(usernameToVerify) == 0):
				print "Other"
				return redirect('/login')
			elif(request.form['password'] == usernameToVerify[0]['password']):
				session['loggedinName'] = usernameToVerify[0]['firstname'] + ' ' + usernameToVerify[0]['lastname']
				session['username'] = usernameToVerify[0]['username']
				return redirect('/newsFeedStuff')
			else:
				print usernameToVerify
				return redirect('/login')

		except pymongo.errors.ConnectionFailure, e:
			print "Could not connect to MongoDB: %s" % e
			return redirect('/index')
	else:
		return render_template('login.html', title='Sign In', form=form)


@app.route('/newsFeedStuff', methods=['GET', 'POST'])
def newsFeedStuff():
	if (session.get('loggedinName') == None):
		return redirect('/index')
	form = ReviewForm()
	if form.validate_on_submit():
		try:
			conn=pymongo.MongoClient()
			db = conn.nets
			userInfo = db.userInfo
			myUser = list(userInfo.find({'username' : session['username']}))
			myUser = myUser[0]
			userInfo.remove({'username' : session['username']})
			myUser['reviews'][request.form['name']] = request.form['rate']
			userInfo.insert(myUser)
			return redirect('/newsFeedStuff')
		except pymongo.errors.ConnectionFailure, e:
			print "Could not connect to MongoDB: %s" % e
			return redirect('/newsFeedStuff')
	else:
		try:
			conn=pymongo.MongoClient()
			db = conn.nets
			userInfo = db.userInfo
			myUser = list(userInfo.find({'username' : session['username']}))
			myUser = myUser[0]
			return render_template('newsFeedStuff.html', title='Sign Up', form=form, session = session, rev = myUser['reviews'])
		except pymongo.errors.ConnectionFailure, e:
			print "Could not connect to MongoDB: %s" % e
			return redirect('/newsFeedStuff')



@app.route('/signout', methods=['GET', 'POST'])
def signout():
	session['loggedinName'] = None
	return redirect('/index')

@app.route('/clear',methods=['GET', 'POST'])
def clear():
	try:
		conn=pymongo.MongoClient()
		db = conn.nets
		userInfo = db.userInfo
		userInfo.remove({})
		return redirect('/index')
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		return redirect('/index')