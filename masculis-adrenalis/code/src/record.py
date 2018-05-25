from flask_login import login_user
from .Event import Event, Course, Seminar, Session
from .EventSystem import EventSystem
from .User import User, Staff
import csv

def bootstrap_system():
    system = EventSystem()
    #print("YO")
	
    with open('user.csv') as csvfile:
        #reader = csv.DictReader(csvfile)
        #print("Hello")
        for name in csvfile:
            my_list = name.split(",")
            if 'trainee' in name:
                #print(my_list[0])
                system.add_user(User(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4]))
            if 'trainer' in name:
                system.add_user(Staff(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4]))

    system.create_Course("courseTitle", "presenter", 0, 0, 0, 0, "venue", 5, "description", "status", system.numEvents(), 0)
    system.create_Course("courseTitle2", "presenter", 0, 0, 0, 0, "venue", 5, "description", "status", system.numEvents(), 0)
    return system
