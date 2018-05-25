from abc import ABC, abstractmethod
from .User import User, Staff
from .Event import Event, Course, Seminar

class EventSystem(ABC):
    def __init__(self):
        self.users = []
        self.openCourse = []
        self.openSeminar= []
        self.allEvents = []
        #self.eventNum = 0
    def add_user(self, new_user):
        self.users.append(new_user)

    def get_user_by_id(self, user_id):
        for c in self.users:
            if c.get_id() == user_id:
                return c
        return None

    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user

    def validate_login(self, zID, password):
        for c in self.users:
            if int(c._zID) == int(zID) and c._password == password:
                return c
        return None

    def register_user(self, new_user):
        self.user.append(new_user)

    def deregister_user(self, curr_user):
        self.user.remove(curr_user)

    def create_Course(self, courseTitle, presenter, date, deregDate, startTime, endTime, venue, MaxCapacity, description, status, eventNum, registerFlag):
        newCourse = Course(courseTitle, presenter, date, deregDate, startTime, endTime, venue, MaxCapacity, description, status, eventNum, registerFlag)
        if newCourse != None:
            return newCourse
        else:
            return None

    def create_Seminar(self, seminarTitle, presenter, startDate, endDate, deregDate, startTime, endTime, venue, MaxCapacity, SessNum, description, status, eventNum, registerFlag):
        newSeminar = Seminar(seminarTitle, presenter, startDate, endDate, deregDate, startTime, endTime, venue, MaxCapacity, SessNum, description, status, eventNum, registerFlag)

        print("sem is created")

        if newSeminar != None:
            return newSeminar
        else:
            return None

    def numEvents(self):
        num = 0
        for c in self.allEvents:
            num += 1
        return num

    def addCourse(self, Course):
        self.openCourse.append(Course)
        self.allEvents.append(Course)
    def addSeminar(self, Seminar):
        self.openSeminar.append(Seminar)
        self.allEvents.append(Seminar)

    def get_course(self):
        return self.openCourse

    def get_seminar(self):
        return self.openSeminar

    def get_allEvents(self):
        return self.allEvents

    def get_allEvents(self):
        return self.allEvents

    def get_event(self, eventNum):
        for details in self.get_allEvents():
            print("test")
            if int(details.eventNum) is int(eventNum):
                return details
        return None





