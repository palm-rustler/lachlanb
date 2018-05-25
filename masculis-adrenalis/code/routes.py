from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from server import app, system
from src.User import User, Staff
from src.Event import *

@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form["username"]
        password = request.form["password"]
        new_user=system.validate_login(user_id, password)
        if new_user != None:
            login_user(new_user)
            if isinstance(new_user, Staff):
                return render_template('home.html', trainer = 1)
            else:
                return render_template('home.html')
    return render_template('login.html')

@app.route('/home')
def dashboard():
    course = system.get_course()
    newUser = system.get_user(current_user.name)
    AttList = newUser.get_attend()
    return render_template('home.html', events = AttList)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html')

@app.route('/type', methods=['GET', 'POST'])
def eventType():
    if request.method == 'POST':
        Type = request.form.get('type')

        if Type == 'Course':
            return redirect(url_for('CreateCourse'))
        elif Type == 'Seminar':
            return redirect(url_for('CreateSeminar'))
        elif Type == 'Session':
            return redirect(url_for('CreateSession'))
    return render_template('chooseEvent.html')

@app.route('/CreateCourse', methods=['GET', 'POST'])
def CreateCourse():
    if request.method == 'POST':
        courseTitle = request.form['title']
        presenter = request.form['presenter']
        print(courseTitle)
        print(presenter)
        #dateFormat = "%Y-%m-%d"
        New_date = request.form['date']
        #print(New_date)
        deregDate = request.form['deregDate']
        #print(deregDate)
        #timeFormat= "%H:%M"
        startTime = request.form['startTime']
        print(startTime)
        endTime = request.form['endTime']
        print(endTime)
        venue = request.form['venue']
        print(venue)
        MaxCapacity = request.form['MaxCapacity']
        print(MaxCapacity)
        description = request.form['description']
        print(description)
        status = 1         # Open Event
        eventNum = system.numEvents() + 1
        registerFlag = 0
        Course = system.create_Course(courseTitle, presenter, New_date, deregDate, startTime, endTime, venue, MaxCapacity, description, status, eventNum, registerFlag)
        Users = system.get_user(current_user.name)
        Users.addConvenor(Course)
        if Course != None:
            system.addCourse(Course)
            return render_template('home.html')

    return render_template('CreateCourse.html')

@app.route('/CreateSeminar', methods=['GET', 'POST'])
def CreateSeminar():
    if request.method == 'POST':
        seminarTitle = request.form['title']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        deregDate = request.form['deregDate']
        startTime = 0
        endTime = 0
        venue = request.form['venue']
        MaxCapacity = request.form['MaxCapacity']
        SessNum = 0
        description = request.form['description']
        status = 1
        eventNum = system.numEvents() + 1
        registerFlag = 0
        presenter = current_user.name
        print(presenter)
        Seminar = system.create_Seminar(seminarTitle, presenter, startDate, endDate, deregDate, startTime, endTime, venue, MaxCapacity, SessNum, description, status, eventNum, registerFlag)
        Users = system.get_user(current_user.name)
        Users.addConvenor(Seminar)
        if Seminar != None:
            system.addSeminar(Seminar)
            return render_template('home.html')
    return render_template('CreateSeminar.html')


@app.route('/OpenedEvent')
@login_required
def OpenedEvent():

    seminar = system.get_seminar()
    course = system.get_course()
    user = system.get_user(current_user.name)

    if isinstance(user, Staff):
        return render_template('OpenedEvent.html', seminar=seminar,course=course, trainer = 1)

    return render_template('OpenedEvent.html', seminar=seminar, course=course)

@app.route('/ShowCourse/<eventNum>')
@login_required
def ShowCourse(eventNum):
    details = system.get_event(eventNum)
    newUser = system.get_user(current_user.name)
    isStaff = 0
    if isinstance(newUser, Staff):
        myEvent = newUser.myEvent()
        for eve in myEvent:
            if int(eve.eventNum) == int(details.eventNum):
                isStaff = 1 

    else:
        myAttend = newUser.get_attend()
        for att in myAttend:
            if int(att.eventNum) == int(eventNum):
                isStaff = 1
    isStaff = 0
    if isStaff == 1:
        return render_template('404.html')
    else:
        return render_template('ShowCourse.html', detail = details)

@app.route('/ShowSeminar/<eventNum>', methods=['GET', 'POST'])
@login_required
def ShowSeminar(eventNum):
    details = system.get_event(eventNum)
    convenor = False
    print(current_user.name)
    print(details.presenter)
    if current_user.name == details.presenter:
        convenor = True
    if request.method == 'POST':
        sessionTitle = request.form['title']
        presenter = request.form['presenter']
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        date = request.form['date']
        description = request.form['description']
        details.addSession(sessionTitle, presenter, date, startTime, endTime, description)

    print("SessNum: {}".format( details.SessNum))
   
    return render_template('ShowSeminar.html', detail = details, convenor = convenor)

@app.route('/AfterRegister/<eventNum>')
@login_required
def AfterRegister(eventNum):
    details = system.get_event(eventNum)
    User = system.get_user(current_user.name)
    if User != None:
        User.remove_attend(details)
    return render_template('AfterReg.html', detail = details)

@app.route('/AfterRegisterSess/<eventNum>/<SessNum>')
@login_required
def AfterRegisterSess(eventNum, SessNum):
    details = system.get_event(eventNum)
    details.registerFlag = 0
    foo = details.get_sess(SessNum)
    User = system.get_user(current_user.name)    
    print("eventNum: {}".format( details.eventNum))
    return render_template('AfterReg.html', detail = details, foo = foo)

@app.route('/RegistrationSuccess/<eventNum>/<SessNum>')
@login_required
def RegistrationSuccessSession(eventNum, SessNum):
    
    details = system.get_event(eventNum)
    foo = details.get_sess(SessNum)

    User = system.get_user(current_user.name)
    if User != None:
        User.add_attend(foo)
    return render_template('RegistrationSuccess.html')

@app.route('/deregisterSession/<eventNum>/<sessNum>')
@login_required
def deregisterSession(eventNum, sessNum):
    
    details = system.get_event(eventNum)
    foo = details.get_sess(sessNum)

    User = system.get_user(current_user.name)
    if User != None:
        User.remove_attend(foo)
    return render_template('home.html')

@app.route('/RegistrationSuccess/<eventNum>')
@login_required
def RegistrationSuccess(eventNum):
    details = system.get_event(eventNum)
    User = system.get_user(current_user.name)
    if User != None:
        User.add_attend(details)
    return render_template('RegistrationSuccess.html')











