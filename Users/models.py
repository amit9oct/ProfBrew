"""
Author: Amitayush Thakur, Sagar Graover and Abhimanyu Siwach
This file contains various models for our databases.
"""
from django.db import models

#Some Important Parameters
MAX_LEN_OF_USERNAME=15
MAX_LEN_OF_NAME=200
MAX_LEN_OF_PASSWORD=30

UserType = (
    ('s', 'STUDENT'),
    ('p', 'PROFESSOR'),
    ('v', 'VISITOR'),
)

class Users(models.Model):
    """
        Users()- Extends models.Model. 
        The User class is meant for storing the details of the users into database and keep track of the users.
    """
    def __init__(self):
        #To add to the database
        self.username=models.CharField(max_length=MAX_LEN_OF_USERNAME)
        self.name=models.CharField(max_length=MAX_LEN_OF_NAME)
        self.password=models.CharField(max_length=MAX_LEN_OF_PASSWORD)
        self.user_type=models.CharField(max_length=1,choices=UserType)
        self.email=models.EmailField;
    def __str__(self):
        return self.name
    def is_registered_user(self):
        if self.username!=None and self.name!=None and self.email!=None and self.Type!=UserType.VISITOR:
            return True
        else:
            return False