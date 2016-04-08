# recommendr
**Readme**

Group Members: Selma Belghiti, Deep Kapur, Tahmid Shahriar

Overview:

We are creating a platform to recommend movies and TV shows to people
based on how others with similar tastes recommend them.

Main components:

Data Aggregation: Our data consists of two parts, information on the
movies and tv shows, and information on how people rate them. The first
comes from extracting data from public databases such as IMDb, TMDb,
IMDbTV, and TVDB. The second will include a HIT for crowd workers to
rate movies and tv shows, and collecting data from users on our site as
they sign in or use the site in the future.

Quality Control: We will maintain a quality score for each worker and
user, which will be adjusted based on how other people react to their
recommendations / ratings, i.e. if user U says they really liked movies
A, B, C, D and user  V who really likes A, B, and C, decides to watch D
and likes it, the quality score of U will increase accordingly. This
will help rebalance recommendations through feedback received upon
taking recommendations from the site, and help provide more accurate
results in the future.

(Part 2 submission)
~/scripts contains our mock data for testing both the aggregation and the QC (mockData, qc_test), along with scripts for data aggregation (csvToUser) and QC (quality). We have also found othe key database that we plan on using during the project (movies.csv, ratings.csv) pulled from an online database (IMDB).

Project outline

1.  Collect data from IMDb and TMDb on movies, including all relevant
    information

2.  Collect similar data from IMDbTV and TVDB on tv shows

3.  **Aggregation Module:** Create a HIT to aggregate workers’
    preferences on movies and tv shows they like.

4.  Build out website

5.  Continue to aggregate data through new users who provide quality
    scores on movies - converted into recommendations

6.  **Quality Control Module:** use feedback from users to readjust
    quality of recommendation - providing bonuses to crowd workers or
    other incentives for users for a legitimate recommendation or reduce
    quality score of user if feedback is negative

7.  Aggregate more data on patterns of users based on previous
    preferences and feedback, and use this to further enhance QC and
    recommendations

Milestones:

1.  Collecting initial data - 2 points

2.  Execute HIT on CrowdFlower and collect relevant data - 2 points

3.  Algorithm of using aggregated data to produce relevant insights - 2
    points

4.  Website and infrastructure - 8 points

5.  Quality control model - 4 points

User Workflow: Steps for the user to progress through the app

1.  User goes to our website

2.  User either logs in (step 5) or signs up (step 3)

3.  When user signs up he is prompted to fill out a questionnaire to
    rate 10 movies and 10 TV shows

4.  Once users fills out the form, he is able to go to our general
    website (user who logs in goes directly here)

5.  The website will display some suggestions top 5 suggestions in each
    category

6.  The user is able to search for a specific movie/tv show or category
    (by title, genre, year, type) which returns info on the specific
    title (step 8) or returns a list ranked by order of how likely they
    are to like them

7.  When they click on the movie they will be provided with users
    reviews of these movies (?) and more information (actors, summary
    length of movie etc→ information found in IMDB).

    1.  Show review in order of “helpfulness” a metric used to rank
        > reviews based on how much people like the reviews and the
        > quality score of the reviewer

8.  The user has indicated that he will watch the movie/TV show (step 9)
    etc OR decides to go back and search (back button)

9.  The next time he logs in, they will be asked if they watched the
    last suggestion. If yes, then 10, if no then step 5.

10. Guided to a feedback form to provide us with their rating and review

This leads to the following components on the website:

1.  Main landing page

    1.  Links to log in, sign up

    2.  General description of site


2.  Log in page

    1.  Standard username + password

Can consider captcha as well to avoid security issues

3.  Sign up page

    1.  Form of information relevant to profiling the user
    2.  Survey on how they rate at least 10 movies and tv shows

4.  Homepage

    1.  Search bar
    2.  Top 5 recs in each category

5.  Query page, showing results for the user

6.  Unique landing pages for each movie / tv show

7.  Further support pages

    1.  My account / Profile
    2.  Support
    3.  About Recommendr
