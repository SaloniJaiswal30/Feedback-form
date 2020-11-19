# Feedback-form
A web based project, based on feedback using Flask Framework in which students give the feedback to the faculty after getting registered by faculty. Faculty can see the feedback of students in the form of graphs.

## Technologies Used
- python
- HTML,CSS
- Flask Framwork
- Database: Mysql

## Introduction
This feedback form can be logged in by student and faculty. Student will only able to logging if that student has been registered by faculty and on specific days(change the date accordingly in code else it will give TimeOut message) and can give the feedback to the faculty, on the basis of 20 parameters. faculty can login, register the student and see the feeback of student in the form of graphs.Total 21 graphs are created. So each graph shows how many student has given 5 points, how many given 4, likewise till 1.

## Requirement
- Anaconda Platform(Spyder IDE) has been used therefore .html file should be in side .spyder-py3/templates/. This location path is given to flask inside the code and need to modify according to your system path.
- Flask(conda install -c anaconda flask) and mysql(conda install -c auto flask-mysql) installed using anaconda prompt
- A database is required before running this project. 3 Tables are required form,faculty, detail.Form and faculty are required for login and detail are required to store feedback of student on 20 different parameters.Create Tables:(Database creation is not in this project as of now)
  - form(char student_name,char password,char allowed)
  - faulty(char faculty_name,password). 
  - detail(integer one... integer twenty)(have 20 columns)
  
## Instructions to run
- Run the code(acn.py) and open in localhost:5000	
- Student login if the student is registered then only he can log in.
- There is one more constraint that is student log in on valid dates then only he can fill the form.	
- After login student give his feedback.	
- Faulty can also login if id and password are valid.
- Faculty can register student by just giving name of student.	
- Faculty can see the graph of the no. student given what marks by clicking on the button.There are individual graphs according to questions and also a combine graph of 20 questions are there.
	
		



