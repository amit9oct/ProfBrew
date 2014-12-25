"""
Author: Amitayush Thakur, Sagar Grover and Abhimanyu Siwach
This file contains various models for our databases.
"""
from django.db import models

#Some Important Parameters
MAX_LEN_OF_USERNAME=15
MAX_LEN_OF_NAME=200
MAX_LEN_OF_PASSWORD=30
MAX_LEN_OF_UNIV_NAME=100
MAX_LEN_OF_CLG_NAME=100
MAX_LEN_OF_DEG_NAME=100
MAX_LEN_OF_DIS_NAME=100
MAX_LEN_OF_PROF_QUALIFICATION=200
MAX_LEN_OF_PROF_INTEREST=200
MAX_LEN_OF_PROF_COURSES=200

USER_TYPE = (
    ('STUDENT','Student'),
    ('PROFESSOR','Professor'),
    ('VISITOR','Visitor'),
)

class Users(models.Model):
    """
        Users()- Extends Django's pre-implimented User class. 
        The User class is meant for storing the details of the users into database and keep track of the users.
    """
    def __init__(self):
        #To add to the database
        """
            _username -> private field and is the primary key.
            name -> has the name of the person. It is public.
            _password -> private and encrypted.
            _email -> private field and has valid email address.
            user_type -> has the user type and is public.
            _mobile_number -> private and is the only optional field
        """
        self._username = models.CharField(primary_key=True,max_length=MAX_LEN_OF_USERNAME)  #Primary Key
        self.name = models.CharField(max_length=MAX_LEN_OF_NAME)
        self._password = models.CharField(max_length=MAX_LEN_OF_PASSWORD)
        self.user_type = models.CharField(max_length=10,choices=USER_TYPE,default=USER_TYPE.VISITOR)
        self._email = models.EmailField;
        self._mobile_number = models.BigIntegerField  #Optional Field
        self._date_joined = models.DateTimeField
    def __str__(self):
        """
            __str__()- returns the name of the user
        """
        return self.name
    def get_email(self):
        return self._email
    def get_mobile_number(self):
        return self._mobile_number
    def get_name(self):
        return self.name
    def get_user_type(self):
        return self.user_type
    def get_username(self):
        return self._username
    def get_join_date_time(self):
        return self._date_joined
    def update_name(self,name):
        self.name=name
    def update_username(self,username):
        self._username=username
    def update_password(self,password):
        self._password=password
    def update_email(self,email):
        self._email=email
    def update_mobile_number(self,number):
        self._mobile_number=number
    def update_type(self,user_type):
        self.user_type=user_type
        
class Student(Users):
    """
        Student()- Extends Users(). It represents the student community.
        The database has some new fields like credibility which depends on how much student 
        contributes in ratings.
        We can add a fields like "Discipline" and "Degree Being Pursued"  
    """
    def __init__(self):
        """
            _conributing_factor -> is the measure of student's contribution in updating website info.
                                   It is calculated using a an algorithm.
            _degree_persued -> is the name of the degree being pursued by the student.
                               *Suggestion: Change it to Enum
            _discipline -> is the name of the discipline of the student.
        """
        super(Student,self).__init__(self)
        self._contributing_factor = models.BigIntegerField;
        self._university = models.CharField(max_length=MAX_LEN_OF_UNIV_NAME)  #Should be foreign key
        self._college = models.CharField(max_length=MAX_LEN_OF_CLG_NAME)      #Should be a foreign key
        self._degree_pursued = models.CharField(max_length=MAX_LEN_OF_DEG_NAME)
        self._discipline = models.CharField(max_length=MAX_LEN_OF_DIS_NAME)
    def get_contributing_factor(self):
        return self._contributing_factor
    def get_university(self):
        return self.unversity
    def get_college(self):
        return self._college
    def update_contributing_factor(self,contributing_factor):
        self._contributing_factor=contributing_factor
    def update_university(self,university):
        self._university=university
    def update_college(self,college):
        self._college=college

class Professor(Users):
    """
        Professor()- Extends Users(). It represents the professors of various colleges.
        The database has some new fields like ratings which depends on the overall performance of the 
        professor and the way he is rated by the students of the respective college.
    """
    def __init__(self):
        """
            _ratings -> has the compact rating of the professor
        """
        super(Professor,Users).__init__(self)
        self._ratings = models.BigIntegerField  
        self._university = models.CharField(max_length=MAX_LEN_OF_UNIV_NAME)
        self._college = models.CharField(max_length=MAX_LEN_OF_CLG_NAME)  #Should Be Foreign Key
        self._qualifications = models.CharField(max_length=MAX_LEN_OF_PROF_QUALIFICATION)
        self._area_of_interest = models.CharField(max_length=MAX_LEN_OF_PROF_INTEREST)
        self._courses_teaching = models.CharField(max_length=MAX_LEN_OF_PROF_COURSES)
        self._best_known_for = models.CharField(max_length=MAX_LEN_OF_PROF_COURSES)
        self._popular_name = models.CharField(max_length=MAX_LEN_OF_NAME)
    def get_university(self):
        return self._unversity
    def get_college(self):
        return self._college
    def get_popular_name(self):
        return self._popular_name
    def get_area_of_interest(self):
        return self._area_of_interest
    def get_courses_teaching(self):
        return self._courses_teaching
    def get_best_known_for(self):
        return self._best_known_for
    def get_ratings(self):
        return self._raitngs
    def get_qualifications(self):
        return self._qualifications
    def update_qualifications(self,qualifications):
        self._qualifications=qualifications
    def upadate_college(self,college):
        self._college=college
    def update_area_of_interest(self,interest):
        self._area_of_interest=interest
    def update_best_known_for(self,known_for):
        self._best_known_for=known_for
    def update_courses_teaching(self,courses):
        self._courses_teaching=courses
    def update_popular_name(self,name):
        self._popular_name=name
    def update_university(self,university):
        self._university=university
    def update_ratings(self,ratings):
        self._ratings=ratings