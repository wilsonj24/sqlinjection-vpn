# Instructions

1. First, navigate to the cs.allegheny.edu website and boot up the web server. In order to do so, make sure you have python installed on your machine. You can check to see if you do by opening a terminal window and typing python --version. If you do not have python installed, you can simply go download python from their website https://www.python.org/downloads/ and download the version for your machine.


2. Once you have the server up and running and you can see the site, navigate through the site to get a feel for everything. You can see the site is acting like a bank with a home page, an about page, and a login page. Make sure to read through some of the material to get an idea of what this bank is trying to offer you.


3. After you have navigated through the bank's site and have an idea and an understanding of what it is the bank is trying to offer, the next step is the fun part. Let us try and hack this bank to see if we can extract any important data. Security is a very important measure when it comes to banking as it deals with very valuable information that could be harmful it used in an improper way.


4. As mentioned in the introduction, there are a few different types of methods you can use to hack a database. Just to be clear, we are trying to bypass the database associated with this site, so navigate to the page on the site where you think the hack can take place. This website offers lots of different types and techniques that will allow for this hack to happen https://www.wikihow.com/Hack-a-Database. Be sure to explore and play around with all of these different types of exploits.

5. After you have played around with the different types of exploits, lets try to bypass the forum and extract data from the database. Try typing in ` '` in the username box and press enter. Did you get an error? Now type in `"` and press enter. Did you get an error this time? If so, we have completed our first step to bypassing the login.

6. A big thing that is associated with databases is queries and the syntax of a query statement. Look back at the introduction document and specifically look at the example queries listed there. If the syntax is slightly off the database won't recognize it and this hack will not work. After you have done so, hit the back button on the web browser and go back to the login page.

7. There are a few common SQL injection statements. A big one is `or 1=1`. This statement simply makes everything always equal true. it doesn't matter what you put before this, `or 1=1` will always make the statement be true. Try putting this in along with `"` in the username box. Were you able to bypass the login with this SQL statement? If not we can try something else to bypass the login.

8. One more thing that is associated with SQL injection and SQL statements are inline comments. Usually you just add comments when you want to explain code but don't actually want that segment of code to run. For this particular query though, we need put a comment at the end of this statement in order for it to run. Trying putting  `#`, `/*`, `*/`, `--` at the end of the query statement to see if you can get your SQL injection query to work. Did one of them work? Did they all work. Make sure to answer the questions associated with this lab and keep in mind the ethical implications that go along with SQL injection and hacking.
