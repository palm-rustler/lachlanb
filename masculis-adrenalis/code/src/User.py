from flask_login import UserMixin
from abc import ABC, abstractmethod
from .Event import *

class User(UserMixin):

    def __init__(self, name, zID, email, password, roletype):
        self._name = name
        self._zID = zID
        self._email = email
        self._password = password
        self._roletype = roletype
        self.convenor = []
        self.attend = []

    @property
    def name(self):
        return self._name

    @property
    def zID(self):
        return self._zID

    @property
    def password(self):
        return self._password

    @property
    def email(self):
        return self._email

    @property
    def roletype(self):
        return self._roletype

    @property
    def is_active(self):
        return True

    def get_id(self):
        """Required by Flask-login"""
        return str(self._zID)

    '''def __str__(self):
        return "Student Details: Name - ({0}, Password - {1})"\
                .format(self._username, self._password)'''
    def addConvenor(self, Events):
        self.convenor.append(Events)

    def get_attend(self):
        return self.attend

    def add_attend(self, Events):
        self.attend.append(Events)
        

    def remove_attend(self, Events):
        self.attend.remove(Events) 

class Staff(User):
    def __init__(self, name, zID, email, password, roletype):
        super().__init__(name, zID, email,password, roletype)
        self.convenor = []

    def myEvent(self):
        return self.convenor

    def is_staff(self):
        return True

    '''def __str__(self):
        return "Staff Details: username - ({0}, Password - {1})"\
                .format(self._username, self._password)'''
