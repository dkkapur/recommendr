from quality import fixPoints
from csvToUser import User
a = User("tahmid","shahriar","tahmids@seas.upenn.edu","male","group2","philadelphia","m1","m2","m3","m4","m5","t1","t2","t3","t4","t5")
b = User("sanjid","shahriar","sanjid@seas.upenn.edu","male","group2","philadelphia","m1","m2","m3","m4","m7","t1","t2","t3","t4","t7")
# user_b_viewed = "t5"
user_b_review = 1
fixPoints([a], user_b_review)
print a.qa_score