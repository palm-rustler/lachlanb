from abc import ABC

class Event(ABC):
    def __init__(self, presenter, date, deregDate, startTime, endTime, venue, MaxCapacity, description, status, eventNum, registerFlag):
        self.presenter = presenter
        self.deregDate = deregDate
        self.startTime = startTime
        self.endTime = endTime
        self.venue = venue
        self.MaxCapacity = MaxCapacity
        self.description = description
        self.attendeeList = []
        self.status = status
        self.eventNum = eventNum
        self.registerFlag = registerFlag
        #self.type_ = type_
        #self.convener = convenerID

    def presenter(self):
        return self.presenter

    def deregDate(self):
        return self.deregDate

    def startTime(self):
        return self.startTime

    def endTime(self):
        return self.endTime

    def venue(self):
        return self.venue

    def MaxCapacity(self):
        return self.MaxCapacity

    def description(self):
        return self.description

    def attendeeList(self):
        return self.attendeeList

class Course(Event):
    def __init__(self, courseTitle, presenter, date, deregDate, startTime, endTime, venue, MaxCapacity, description, status, eventNum, registerFlag):
        super().__init__(self, presenter, deregDate, startTime, endTime, venue, MaxCapacity, description, status, eventNum, registerFlag)
        self.courseTitle = courseTitle
        self.date = date

    def get_CourseTitle(self):
        return self.courseTitle

    def date(self):
        return self.date

    def __str__(self):
        return "Title: {} || Venue: {} || Description: {} || Max. Capacity: {} || Date: {} || Start Time: {} || End Time {} || Deregister Before: {}".format(self.courseTitle, self.venue, self.description, self.MaxCapacity, self.date, self.startTime, self.endTime, self.deregDate)

class Seminar(Event):
    def __init__(self, seminarTitle, presenter, startDate, endDate, deregDate, startTime, endTime, venue, MaxCapacity, SessNum, description, status, eventNum, registerFlag):
        super().__init__(self, presenter, deregDate, startTime, endTime, venue, MaxCapacity, description, status, eventNum, registerFlag)
        self.seminarTitle = seminarTitle
        self.startDate = startDate
        self.endDate = endDate
        self.SessNum = SessNum
        self.sessions = []
        self.eventNum = eventNum
        self.presenter = presenter
    def addSession(self, seminarTitle, presenter, date, startTime, endTime, description):
        session = Session(seminarTitle, presenter, date, startTime, endTime, description)
        self.SessNum = self.SessNum + 1
        session.SessNum = self.SessNum        
        session.eventNum = self.eventNum        
        self.sessions.append(session)
        

    def get_SeminarTitle(self):
        return self.seminarTitle

    def get_startDate(self):
        return self.startDate

    def get_endDate(self):
        return self.endDate

    def get_SessNum(self):
        return self.SessNum

    def get_sess(self, SessNum):
        for details in self.sessions:
            if int(details.SessNum) is int(self.SessNum):
                return details
        
    def __str__(self):
        return "Event Details : Title: {} || Convenor: {} || Venue: {} || Description: {} || Max. Capacity: {} || Start Date: {} || End Date: {} || Start Time: {} || End Time {} || Deregister Before: {}".format(self.seminarTitle, self.presenter, self.venue, self.description, self.MaxCapacity, self.startDate, self.endDate, self.startTime, self.endTime, self.deregDate)

class Session(Seminar):
    def __init__(self, seminarTitle, presenter, date, startTime, endTime, description, SessNum=0, eventNum=0):
        self.seminarTitle = seminarTitle
        self.presenter = presenter
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.description = description
        self.SessNum = SessNum
        self.eventNum = eventNum
		
    def __str__(self):
        return "Session Details: {} || Presenter: {} || Description: {} || Date: {} || Time: {} - {}".format(self.seminarTitle, self.presenter, self.description, self.date, self.startTime, self.endTime)















