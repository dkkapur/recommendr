import math
from csvToUser import User
a = User("tahmid","shahriar","tahmids@seas.upenn.edu","male","group2","philadelphia","m1","m2","m3","m4","m5","t1","t2","t3","t4","t5")
# we know the users who we are basic it off
def fixPoints(usersWhoRecommended, reviewOfViewer):
	if reviewOfViewer == 1:
		for x in range(0, len(usersWhoRecommended)):
			usersWhoRecommended[x].qa_score = usersWhoRecommended[x].qa_score + 0.1
	else:
		for x in range(0, len(usersWhoRecommended)):
			usersWhoRecommended[x].qa_score = usersWhoRecommended[x].qa_score - 0.1
			if usersWhoRecommended[x].qa_score < 0:
				usersWhoRecommended[x].qa_score = 0
