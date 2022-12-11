
class User: 
    username = ""
    password = ""
    events = []
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def addEvent(self, event):
        for i in self.events:
            if i.eventName == event.eventName:
                print("Event Name must be unique")
                return False
        self.events.append(event)
        return True

    def delEvent(self, event):
        for i in self.events:
            if i.eventName == event.eventName:
                self.events.remove(i)
                return True
        return False

class Event:
    eventName = ""
    timeHrs = 0
    timeMin = 0
    dateMonth = 0
    dateDay = 0
    dateYear = 0
    description = ""

    def __init__(self, eventName, timeHrs, timeMin, dateMonth, dateDay, dateYear, descripition):
        self.eventName = eventName
        self.timeHrs = timeHrs
        self.timeMin = timeMin
        self.dateMonth = dateMonth
        self.dateDay = dateDay
        self.dateYear = dateYear
        self.descripition = descripition

class Day:
    dayName = ""
    dateMonth = 0
    dateDay = 0
    dateYear = 0
    events = []

    def __init__(self, dayName, dateMonth, dateDay, dateYear, events):
        self.dayName = dayName
        self.dateMonth = dateMonth
        self.dateDay = dateDay
        self.dateYear = dateYear
        self.events = events

class Week:
    days = []

    def __init__(self, days):
        self.days = days