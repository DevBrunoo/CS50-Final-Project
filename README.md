# CS50 final project

#### Video Demo: https://youtu.be/JITfIHabZy8
#### Description: Final project cs50, about time management
This is a web application that is based on helping you organize and value every minute of your time, we all know how precious our time can be and we should value every second of it, but there are few tools that help us with this task.

The project's function is to serve as an agenda and show several motivational phrases to the user during the day, the data filled in the forms are stored in an SQL database. The website design was built using the bootstrap framework.

# Amostra do site

![](https://i.giphy.com/media/LEjDWeFaCSKvQzYcxO/giphy.webp)

# CSS Board

Cascading Style Sheets is a mechanism for adding style to a web document. CSS code can be applied directly to tags or contained within <style> tags.

It is used in the files to make the project more beautiful, an example is that we do not use style.css to change the style of the page /motivation

# JS Board

JavaScript is a structured, high-level scripting, dynamically typed, multiparadigm, interpreted programming language. Along with HTML and CSS, JavaScript is one of the three main technologies on the World Wide Web.

We use JavaScript in the motivation.html file to create functionality to bring an image along with a message every 3 hours. In other words, we use javascript in this project to implement more functionalities, you can see the JavaScript in the 'app.js' file;

# Python directory

Python is a very popular language in areas of technology related to data analysis, research, algorithm development and AI.

We use Python in this project, to use the Flask framework together with the SQL database. We run the application through Python functions and manage all user information through SQL.

# SQLite

SQLite is a type of relational database, that is, one that creates files based on the relationship between different elements, usually taking the form of a table. However, unlike other models, it does not depend on a server to store its information.

We use it to manage user information, both to delete, add and edit.
     
# Acknowledgment

I would first like to thank the CS50 team for showing me this wonderful world of programming and for teaching me many things that I will take with me throughout my life. Without you, this like other projects I built in my life would not exist

We use Python to import Flask flamework like this along with its libraries
that are useful both for application development and also for interaction
with the SQL database that serves to store and manage the information of our
application.
     https://cs50.harvard.edu/x/2022/

```python

# You have to install the cs50 library via terminal by:

$ pip3 install cs50


```
## Answered questions

1. What will your software do?
     - My web application shows the time for the client, as well as stores information like the agenda and shows several motivational phrases every three hours through the “motivation” file


2. What features will it have?
     - It will have a standard web design created with bootstrap, it will be minimalist and clear


3. How will it be executed?
     - Will be executed via python using a framework called flask


4. What new skills will you need to acquire?
     - It was necessary to acquire more knowledge in JavaScrip to use functions in the manner corresponding to the project, it was also necessary to learn more about structure and design of SQL database.

5. What topics will you need to research?
     - I had to research more about SQLite, JavaScript and CSS



6. If working with two colleagues who for what?
     - I'm not working in pairs unfortunately


7. What can you consider a good result for your project?
     - That it runs easily, that it is intuitive and that it can be optimized for many types of screens and platforms.

8. A better result?
     - Run without crashing on any server and be easy to use
     
8. The best result?
     - That people really start using it for a better life, that it can help a large number of people.



## To rotate

To run the application run the following line commands


```python

# If you don't have Flask installed or are using this app for the first time
cd project

# Will install some project dependencies

python3 -m venv venv 

# To activate the corresponding environment

. venv/bin/activate 

# Will install flask library

pip install Flask

# Will make your web app run. 
# Run this command only if inside the myproject page

flask run

```

If you already have Flask installed or have already accessed this project

```python

cd project

. venv/bin/activate

flask run
```

# Database

Run the following commands to view the data in the database

```bash

# Make sure you have SQL installed on your machine 
# If you don't have it installed on your machine 
# First enter the folder

cd myproject

sqlite3 schedule.db 

# To view calendar data:

SELECT * FROM schedule; 

# To view contact page data;

SELECT * FROM contact;

```


------------------------------------------------------------------------------------------------------------------------
#### Programming and Markup Langugaes:

<a><img class="icons_curve" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"/></a>
<a><img class="icons_curve" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"/></a>
<a><img class="icons_curve" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=black"/></a>
<a><img class="icons_curve" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/></a>
<a><img class="icons_curve" src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/></a>



------------------------------------------------------------------------------------------------------------------------
#### Frameworks:

<a><img class="icons_curve" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white"/></a>
<a><img class="icons_curve" src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white"/></a>


------------------------------------------------------------------------------------------------------------------------
#### CS50 Certificate:
<img src="https://i.ibb.co/1zCkWhj/CS50x.png" alt="CS50x" border="0">

