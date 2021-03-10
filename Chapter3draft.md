### Method Approach Draft
## By: Jordan Wilson



# Method of Approach

The way that I had to complete my proposed research and to also make sure that I had
completed everything that I needed to do was by first planning out what exactly I needed
to do. Since I had decided to do a SQL injection attack, I had to first figure out
what I was going to be attacking. SQL injection attacks are typically done against
web based applications so I had planned on targeting a website to do my attack on. After
figuring out that I had decided to attack a website for my project, I next had to
think of a specific website I could attack in order to properly learn but also
keep in mind that I cannot just perform an attack on any regular website as that would
not be an ethical thing to do. After talking with my readers, the best option that
we had decided was for me to create my own "dummy" website as this would allow
me to be able to not only perform my own SQL injection but to also have the piece of
mind knowing that if I did indeed accidentally made a change to the website that
I would not be harming anybody else's work in the process. I had decided to use
flask for the creation of this website. Although there are other options out there
such as django and streamlit, I chose flask mostly for the familiarity with the design
and also the fact that it uses python as its coding language. When making my website
I had to make the design and layout of the site is not only user-friendly but also make
sure that I included somewhere in the site where the SQL injection could take place.
I created the site to act as a mock-up for what a banking website would look like, just
to try and reel in the user and make the illusion that they are actually on a banking
website with the idea that they are going to inject SQL code in order to by-pass the
security and gain access to sensitive data. After making sure I had done everything
that I wanted to do and the website was created, I had then done my SQL injection attack.



{Insert Website image}



When I had created my "dummy" website and performed the actual SQL injection attack,
I needed to utilize some coding languages as well as databases if I were to properly
and effectively conduct my injection attack. The first coding language
that I had to utilize is HTML. This is imperative because this is the
language that I am going to be using while creating my "dummy" website. HTML simply
stands for hyper-text markup language and this is a web-based language commonly
used when creating a website. I had decided to use HTML because of its easy to understand
language as well as its simplistic syntax. HTML is widely known and used today. The
next and important database language that I had to use was SQL. This should not
be a surprise as the title of my senior thesis is "Assessing vulnerabilities using
SQL injection".


{Insert HTML/SQL code}



When doing my attack, I had to insert SQL queries in order to try and by-pass some
of the log-in administration Credentials. With the information that I had gained from
the research of SQL injection attacks, I had done a various number of attacks to try
and inject code into the SQL statements of the website and gain access to the very sensitive
data that is on the website. Some examples of things that I did were, I thought to myself,
if I were creating a website, what times of SQL statements would I make in order to try
and connect the SQL database to the website in order to try and make it so that the log-in
Credentials would allow someone with the right credentials to log-on and see the
information they are allowed to see. When trying to figure out what type of statement
might have been used in order to connect the database to the site, there were somethings that
I could assume were going to be there. First, SELECT username FROM, is a good guess as to assuming
what parts of SQL statement would be included since we are dealing with customers and workers
because this is considered to be a banking website. So next, I had to try and figure out what may
be on the end of the SQL statement. Well, like I said, since this is considered to be a banking
website with log-in credential information, it probably is close to something like, 'username' +
'password'. From here, I can start making some guesses and estimations on what the SQL statement
might look like, but also how I could possibly inject code into this statement in order
to access this data. Again, with the research that I had stated above in the introduction,
there are a lot of common SQL injection code tries that you could do to bypass a log-in.
With this knowledge, I then started trying different common sql queries in order to
gain access. Low and behold, one of the techniques that I had ended up trying actually
worked.


{Insert SQL Statement Image}


After the SQL injection attack and time permitting, I then started the implementation
for a prototype that allows for better security involving databases. I planned on attaching
my prototype to the associated website that I created and then will show how the prototype
that I created will help guard against not only SQL injection attacks but also other
attacks as well. The two main services that I will use to help create my tool will
first be cloud computing. As we have learned, cloud computing will help with security
measures because, cloud computing will allow for the database to not staticly sit
on a dedicated server or machine, but it will allow for the database to be accessed
through the cloud. The next service or tool that I will use to implement my prototype will
be to use a VPN. From the related work articles, I believe using a VPN will help with
privacy and security as well as it scrambles users ip addresses and location services so
that the user wouldn't be tracked.

When it comes to the VPN and Cloud computing component of the project, I had to make
sure I could use some sort of software that would allow me to integrate both tools.
With much research on this topic, I then came to the conclusion of using Algo VPN
and digitalOcean cloud computing software. These two tools allowed me to setup
a "firewall" of sorts that created an extra layer of security. With the AlgoVPN data
structure, I can create my own server and actually watch and monitor traffic on that
dedicate server myself. So, if anyone tries to access that specific server, I will be
notified. When I pair this with the digitalOcean cloud computing infrastructure, you will
then be forced to login to the cloud in order to access the very sensitive data that
is inside of the database. When you put this all together, this is how it should look
like. The first step in order to access this vital sensitive information would to first
fire up the AlgoVPN and connect to a specific server so that only you could monitor
the traffic (I.E., no one else knowing where you actually are logging onto the database from).
Next, you log-in to the digitalOcean cloud computing platform and put in your credentials (
assuming you have the "rights" to view this database). From there, you should be able to
see the vital information that you don't want other people to see.


{Insert Cloud Computing/VPN image}



There are some concerns that surround this idea as well. The first major concern with SQL
injection is the ethical uses behind it. It is no secret that SQL injection has been
used in the past to harm web-applications, or to steal, alter or delete data that may
be on the website. Another big thing that is relevant to this type of project is
how valid will my findings of my research be? In order to be able to fully address
the validity of my findings, I think it is best to put all of my findings in a table.
In this way I can display all of my findings in an organized manner. I have attached
a screenshot of the steps that I had taken in order to physically show how I had done
these things. In this way, I can have actual physical proof to show that my findings were indeed
accurate to whatever I had stated in my table. The next question asked is how feasible it
would be to have a fully working tool that could possibly not only fix SQL databases
from being susceptible to injection attacks but other attacks as well. I cannot
say that I will have a fully functional tool working at the end of the time allotted
for the project but if I had more time, the possibility of creating a tool that could
help mitigate attacks wouldn't be out of the question. With the time allotted for
me though, I plan to start to work on a prototype that could shed light on possible
ways someone could reduce the risk of SQL based databases being hacked through not only
injection but other techniques as well.
