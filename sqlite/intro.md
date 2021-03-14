# Introduction

In this lab, we will explore the ethical implications that go along with hacking and databases. Lots of databases are out on the web that contain valuable information. What people don't know is that bypassing the security to access data from the database is a lot easier than one might think. For this lab, we will be looking at a website that mirrors what a banks website might look like that has a database connected to it that contains very valuable data. While there are many different techniques that someone may use to hack something, we will specifically be looking into SQL injection. SQL injection is an attack technique that exploits a security vulnerability occurring in the database layer of an application. Hackers use injections to obtain unauthorized access to the underlying data and structure of the system that they are trying to hack.

### How does a SQL injection attack occur?

SQL injection attacks occur when a web application does not validate values received from a web form, cookie, input parameter and more. There are several types of SQL injection but in this lab we are going to focus primarily on SQL injection through user input. Web applications typically accept user input through a form, and the front-end passes the user input to the back-end database for processing. If the web application fails to sanitize user input, an attacker can inject SQL statements of their choice into the back-end of the database basically allowing them to delete, copy, or modify the contents of the database.


### What does this look like?

Below is an example of of query statement being used to run the database on a web application.

``` SELECT * FROM customers WHERE customer_id ='12345' ```

This is simply a query telling the database to select everything from the customers table where the customer id = 12345.

Suppose someone wanted to inject a SQL statement into the query looking something like this.

``` SELECT * FROM customers WHERE customer_id='12345'; DELETE * FROM customers WHERE 'x' = 'x' ```.

This SQL injection statement is basically deleting everything that is in the customers table where there is a value being declared.
