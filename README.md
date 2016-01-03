#Testing Guide

##Installations required for Testing the REST framework: 
### Create the project directory
mkdir testing
cd testing

### Create a virtualenv to isolate our package dependencies locally
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

### Install Django and Django REST framework into the virtualenv
pip install django

pip install djangorestframework

### Install HTTPIE
pip install httpie

###Description: 
A basic REST API service built using Django and Python. The web service works as a simple discussion board where registered users can create topics and add comments to the topic. 
It also allows the registered users to edit the existing comments.
As part of exercise 2 application allows the multiple users to edit the existing comments without losing the information.
It keeps track of the when was the particular content was last modified. So the users get to access the latest comment.

###Unit Testing:
I have created two applications topics and comments. The test cases are included in their respective tests.py file.

#####To run the unit test in command prompt run:

python manage.py test

Testing on Web Browser:

#####To run the application on the web browser:
	
In Command prompt run: python manage.py runserver

1.	Get all registered Users :
Paste the link on browser: http://127.0.0.1:8000/users/ 
 ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/Get_Users.JPG)


2.	Get a particular User:
Paste the link on browser: http://127.0.0.1:8000/users/ 1/
![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/get_particular_user.JPG)
 

	
3.	Get all topics :
Paste the link on browser : http://127.0.0.1:8000/topics/

 ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/get_all_topics.JPG)


4.	Get a particular Topic:
Paste the link on browser : http://127.0.0.1:8000/topics/1/
 ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/get_particular_topic.JPG)


5.	Get all comments of a topic:
Paste the link on browser : http://127.0.0.1:8000/topics/7/comments/
 ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/get_topic_comments.JPG)


6.	Create a Topic :
In command Prompt :
http -a anudeep:123456 --json POST http://127.0.0.1:8000/topics/ title="New Topic" 
![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/Create_Topic.JPG)
 

 
7.	Delete a topic:
In command Prompt :
http -a anudeep:123456 --json DELETE http://127.0.0.1:8000/topics/4/
and 
http://127.0.0.1:8000/topics/4/

 ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/Delete.JPG)


###Comment Section with Etags and Last modified
In a new Command prompt window run the below commands to test the application

1.	Get Comments :

http  -a Anudeep:123456 –json GET http://127.0.0.1:8000/topics/1/comments/3/
 
  ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/Etag_Get.JPG)

2.GET- If_None_Match:

http  -a Anudeep:123456 –json GET http://127.0.0.1:8000/topics/1/comments/3/ “If-None-Match:\“ 4aab95a43eee364d47203fbffc2f5f8d\””
 
   ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/Etag_Get_If_None_Match.JPG)

3.PUT : If-Match header is not passed, the application should prompt user to provide Precondition

http  -a Anudeep:123456 –json PUT  http://127.0.0.1:8000/topics/1/comments/3/ comment=“Modify the Comment with Put Statement”
  ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/Etag_Put_Pre_Condition.JPG)

4.PUT – Invalid Etag is passed: Application throws message PRECONDITION FAILED
http  -a Anudeep:123456 –json PUT  http://127.0.0.1:8000/topics/1/comments/3/ comment=“Modify the Comment with Put Statement” “If-Match:\“ Invalid Value\””
 
 ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/Etag_Put_Pre_Condition_failed.JPG)
5.PUT :

User provides valid credentials along with If-Match header with correct Etag and comment 
http  -a Anudeep:123456 –json PUT  http://127.0.0.1:8000/topics/1/comments/3/ comment=“Modify the Comment with Put Statement” “If-Match:\“ 4aab95a43eee364d47203fbffc2f5f8d\””

  ![alt text](https://github.com/anudeepchen/MyProject/blob/master/Exablox/Etag_Put.JPG)


6.DELETE : Delete follows same rules as PUT statement



