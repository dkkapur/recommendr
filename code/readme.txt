README: How the code works

We're using a standard MVC model powered by Python, and HTML/CSS for the front-end. 

At this stage of our project, we are currently collecting data from users, i.e. classmates and friends who can help populate our database. 
This happens at the signup point, where each person is asked a series of questions with the intent of creating a unique profile in the database for them. 
Revelant files: 
signup.html - what the user sees when they sign up
views.py - controller for the front end
forms.py - data that we collect about each user

The app stores this information in a relevant table in the DB, from where we can access it in the future to provide recommendations. 

The main algorithm will consist of combining information about each user and each movie / tv show in our database to provide better recommendations for each user. 
This is achieved through creating connected components / and testing for homophily across groups of users, that are bucketed based on attributes and information we gather about them. 
There's a lot of research on this, and we plan to use a few of the more revelant papers in making sure our method makes sense. 

TESTING - we are hosting our site at http://final-pgnrush.rhcloud.com/ and it can be viewed at various points in our dev. timeline where we will push the latest updates to it.
