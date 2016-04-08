import csv

class User:
	first_name = None
	last_name = None
	email = None
	gender = None
	age_group = None
	location = None
	movies_liked_id1 = None
	movies_liked_id2 = None
	movies_liked_id3 = None
	movies_liked_id4 = None
	movies_liked_id5 = None
	tv_show_liked_id1 = None
	tv_show_liked_id2 = None
	tv_show_liked_id3 = None
	tv_show_liked_id4 = None
	tv_show_liked_id5 = None
	qa_score = 1
	reviews = {}

	def __init__(self,first_name,last_name,email,gender,age_group,location,movies_liked_id1,movies_liked_id2,movies_liked_id3,movies_liked_id4,movies_liked_id5,tv_show_liked_id1,tv_show_liked_id2,tv_show_liked_id3,tv_show_liked_id4,tv_show_liked_id5):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.gender = gender
		self.age_group = age_group
		self.location = location
		self.movies_liked_id1 = movies_liked_id1
		self.movies_liked_id2 = movies_liked_id2
		self.movies_liked_id3 = movies_liked_id3
		self.movies_liked_id4 = movies_liked_id4
		self.movies_liked_id5 = movies_liked_id5
		self.tv_show_liked_id1 = tv_show_liked_id1
		self.tv_show_liked_id2 = tv_show_liked_id2
		self.tv_show_liked_id3 = tv_show_liked_id3
		self.tv_show_liked_id4 = tv_show_liked_id4
		self.tv_show_liked_id5 = tv_show_liked_id5


myUsers = []
with open('mockData.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	start = False
	for row in spamreader:
		if start == False:
			start = True
		else:
			temp = row[0].split(",")
			add = User(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12],temp[13],temp[14], temp[15]) 
			myUsers.append(add)









