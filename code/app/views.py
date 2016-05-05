from flask import render_template, flash, redirect, request, session
from app import app
from .forms import LoginForm, LunchForm, SignupForm, ReviewForm, SearchForm
import pymongo, time
import csv
import json
import re
import os 
import requests
from random import randint


apik = "100f914c4536b4fb13ba7bc52449c5af"
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
			data['extraverted'] = request.form['extraverted']
			data['agreeable'] = request.form['agreeable']
			data['consc'] = request.form['consc']
			data['emotional'] = request.form['emotional']
			data['experiences'] = request.form['experiences']
			data['pleasureseeking'] = request.form['pleasureseeking']
			data['nostalgia'] = request.form['nostalgia']
			data['catharsis'] = request.form['catharsis']
			data['aggression'] = request.form['aggression']
			data['escapism'] = request.form['escapism']
			data['sensationseeking'] = request.form['sensationseeking']
			data['artistic'] = request.form['artistic']
			data['informationseeking'] = request.form['informationseeking']
			data['boredomavoidance'] = request.form['boredomavoidance']
			data['socialization'] = request.form['socialization']
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
	if (request.method == "POST"):
		session['current'] = request.form['name']
		return redirect("/movie")

	if (session.get('loggedinName') == None):
		return redirect('/index')
	form = SearchForm()
	try:
		conn=pymongo.MongoClient()
		db = conn.nets
		userInfo = db.userInfo
		movieInfo = db.movieInfo
		myMovie = list(movieInfo.distinct('title'))
		myMovie.sort()
		myUser = list(userInfo.find({'username' : session['username']}))
		myUser = myUser[0]
		if len(myUser['reviews']) < 5:
			session['current'] = myMovie[randint(0, len(myMovie))]
			return redirect("/movie")
		if 'watch' in myUser:
			v = myUser['watch']
		else:
			v = []
		return render_template('newsFeedStuff.html', title='Sign Up', form=form, session = session, rev = myUser['reviews'], myMovie = myMovie, watchList = v)
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		return redirect('/newsFeedStuff')



@app.route('/print', methods=['GET', 'POST'])
def userP():
	try:
		conn=pymongo.MongoClient()
		db = conn.nets
		userInfo = db.userInfo
		myUser = list(userInfo.find({}))
		print myUser
		return redirect('/newsFeedStuff')
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		return redirect('/newsFeedStuff')
    


@app.route('/loadMovie', methods=['GET', 'POST'])
def loadU():
	try:
		conn=pymongo.MongoClient()
		db = conn.nets
		movieInfo = db.movieInfo
		for row in csv.DictReader(open( (os.path.join(os.path.dirname(__file__),'movies.csv')) ), delimiter='\t'):
			v = row["movieId,title,genres"]
			myVal = v.split(",")
			data = {}
			try:
				m = myVal[1].split("(")[0]
				m = m.split("\"")
				if len(m) > 1:
					m = m[1]
				else:
					m = m[0]
				if (m[len(m) - 1]) == " ":
					m = m[0:len(m)-1]
				if len(list(movieInfo.find({"title":m}))) == 0:
					res = requests.post('https://api.themoviedb.org/3/search/movie', data={"api_key": "100f914c4536b4fb13ba7bc52449c5af", "query": m})
					res = res.json()
					data["title"] = m
					data["genre"] = myVal[2]
					data["image"] = "http://image.tmdb.org/t/p/w500/" + res['results'][0]['poster_path']
					movieInfo.insert(data)
					print m
			except:
				m = myVal[1].split("(")[0]
				m = m.split("\"")
				if len(m) > 1:
					m = m[1]
				else:
					m = m[0]
				if (m[len(m) - 1]) == " ":
					m = m[0:len(m)-1]
				print "Fail: " + m
				pass
	except pymongo.errors.ConnectionFailure, e:
			print "Could not connect to MongoDB: %s" % e
			return redirect('/loadMovie')

	mov = list(movieInfo.find({}))
	print mov
	return "hi"

@app.route('/movie', methods=['GET', 'POST'])
def mov():
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
			if "watch" in myUser:
				if request.form['name'] in myUser["watch"]:
					myUser["watch"].remove(request.form['name'])
			userInfo.insert(myUser)			
			return redirect("/newsFeedStuff")
		except pymongo.errors.ConnectionFailure, e:
			print "Could not connect to MongoDB: %s" % e
			return "Mongo Failed"
	else:
		if session['current']:
			if session['current'] == "":
				return redirect("/newsFeedStuff")
			title = session['current']
			session['current'] = ""
			session['watch'] = title
			try:
				conn=pymongo.MongoClient()
				db = conn.nets
				movieInfo = db.movieInfo
				userInfo = db.userInfo
				myV = list(movieInfo.find({'title' : title}))
				print "0"
				if len(myV) > 0:
					myV = myV[0]
					myUser = list(userInfo.find({}))
					me = list(userInfo.find({'username' : session['username']}))
					viewed = []
					final = -1
					n = 0
					print "1"
					for u in myUser:
						if title in u['reviews'] and u != me[0]:
							viewed.append(u)
					print "1.5"
					if (len(viewed) > 0):
						final = 0
					print "2"
					for vu in viewed:
						print "hiiiiiiii"
						score = simScore(me, vu)
						rated = vu['reviews'][title]
						print str(score) + " : " + str(rated)
						if rated == "3":
							if score > 0.3:
								final = final + 3
								n = n + 1
						else:
							if score > 0.3:
								final = final + int(rated)
								n = n + 1
							else:
								final = final + (6 - int(rated))
								n = n + 1
					print "3"
					if (n != 0):
						final = round( float(final) / float(n), 0)

				else:
					return "Movie not found"
			except:
				return "welp"
			return render_template('movie.html', title=title, session = session, mov = myV, form = form, final = final)
		else:
			return redirect("/newsFeedStuff")

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






@app.route('/watch', methods=['GET', 'POST'])
def watchL():
	try:
		conn=pymongo.MongoClient()
		db = conn.nets
		userInfo = db.userInfo
		myUser = list(userInfo.find({'username' : session['username']}))
		myUser = myUser[0]
		userInfo.remove({'username' : session['username']})
		if 'watch' in myUser:
			if session['watch'] not in myUser['watch']:
				myUser['watch'].append(session['watch'])
		else:
			myUser['watch'] = [session['watch']]

		userInfo.insert(myUser)			
		session['current'] = session['watch']
		return redirect("/movie")
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e
		return "Mongo Failed"

@app.route('/rate', methods=['GET', 'POST'])
def setReview():
	session["current"] = request.args['myr']
	return redirect ('/movie')



def simScore(me, other):
	me = me[0]
	diff = 0.0
	factor = 0.0
	diff = diff + abs(int(me['extraverted']) - int(other['extraverted']))
	if abs(int(me['extraverted']) - int(other['extraverted'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['extraverted']) - int(other['extraverted'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	diff = diff + abs(int(me['agreeable']) - int(other['agreeable']))
	if abs(int(me['agreeable']) - int(other['agreeable'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['agreeable']) - int(other['agreeable'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	diff = diff + abs(int(me['consc']) - int(other['consc']))
	if abs(int(me['consc']) - int(other['consc'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['consc']) - int(other['consc'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0


	diff = diff + abs(int(me['emotional']) - int(other['emotional']))
	if abs(int(me['emotional']) - int(other['emotional'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['emotional']) - int(other['emotional'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	diff = diff + abs(int(me['experiences']) - int(other['experiences']))
	if abs(int(me['experiences']) - int(other['experiences'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['experiences']) - int(other['experiences'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	d1 = diff/factor


	diff = 0.0
	factor = 0.0
	diff = diff + abs(int(me['pleasureseeking']) - int(other['pleasureseeking']))
	if abs(int(me['pleasureseeking']) - int(other['pleasureseeking'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['pleasureseeking']) - int(other['pleasureseeking'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	diff = diff + abs(int(me['nostalgia']) - int(other['nostalgia']))
	if abs(int(me['nostalgia']) - int(other['nostalgia'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['nostalgia']) - int(other['nostalgia'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0


	diff = diff + abs(int(me['catharsis']) - int(other['catharsis']))
	if abs(int(me['catharsis']) - int(other['catharsis'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['catharsis']) - int(other['catharsis'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0


	diff = diff + abs(int(me['aggression']) - int(other['aggression']))
	if abs(int(me['aggression']) - int(other['aggression'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['aggression']) - int(other['aggression'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0


	diff = diff + abs(int(me['escapism']) - int(other['escapism']))
	if abs(int(me['escapism']) - int(other['escapism'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['escapism']) - int(other['escapism'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0



	diff = diff + abs(int(me['sensationseeking']) - int(other['sensationseeking']))
	if abs(int(me['sensationseeking']) - int(other['sensationseeking'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['sensationseeking']) - int(other['sensationseeking'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	diff = diff + abs(int(me['artistic']) - int(other['artistic']))
	if abs(int(me['artistic']) - int(other['artistic'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['artistic']) - int(other['artistic'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	diff = diff + abs(int(me['informationseeking']) - int(other['informationseeking']))
	if abs(int(me['informationseeking']) - int(other['informationseeking'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['informationseeking']) - int(other['informationseeking'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	diff = diff + abs(int(me['boredomavoidance']) - int(other['boredomavoidance']))
	if abs(int(me['boredomavoidance']) - int(other['boredomavoidance'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['boredomavoidance']) - int(other['boredomavoidance'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0

	diff = diff + abs(int(me['socialization']) - int(other['socialization']))
	if abs(int(me['socialization']) - int(other['socialization'])) > 35:
		factor = factor + 1.5
	elif abs(int(me['socialization']) - int(other['socialization'])) < 10:
		factor = factor + 0.5
	else:
		factor = factor + 1.0
	d2 = diff/factor

	return (100/(d1 + d2))



