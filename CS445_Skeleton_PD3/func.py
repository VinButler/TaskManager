import json
import hashlib


def viewAllEvents(uid):
    #
    # Opens file
    # Finds users uid and lists all events under the user
    #
    with open('events.json','r') as file:
        jsonData = json.load(file)
        for user in jsonData["users"]:
            if user["userID"] == uid:
                for event in user["events"]:
                    print("EventID: ",event["eventID"])
                    print("Name: ",event["name"])
                    print("Day: ",event["day"])
                    print("Time: ",event["time"])
                    print("Duration: ",event["duration"])
                    print("Description: ",event["description"],"\n")

def viewEvent(uid, eid):
    #
    # Opens file
    # Finds users uid and lists specific event under the user
    #
    with open('events.json', 'r') as file:
        jsonData = json.load(file)
        for user in jsonData["users"]:
            if user["userID"] == uid:
                for event in user["events"]:
                    if event["eventID"] == eid:
                        print("EventID: ",event["eventID"])
                        print("Name: ",event["name"])
                        print("Day: ",event["day"])
                        print("Time: ",event["time"])
                        print("Duration: ",event["duration"])
                        print("Description: ",event["description"],"\n") 
                        return True
    return False



def createEvent(uid, name, day, time, duration, description):
    #
    # Takes input from create event button
    # creates dictionary, adds it to a list, 
    # and json dumps it into the json file
    #
    eventarray = []
    eventData = {
        "eventID":1,
        "name":name,
        "day":day,
        "time":time,
        "duration":duration,
        "description":description
    }
    with open('events.json','r+') as file:
        jsonData = json.load(file)
        # is it the first event created under this user?
        if not any(user["userID"]==uid for user in jsonData["users"]):
            event = {
                "userID":uid,
                "events":[
                    eventData
                    ]
            }
            jsonData["users"].append(event)
            file.seek(0)
            json.dump(jsonData,file,indent=4)
            print("Event created")
        # user has pre-exisiting events
        else:
            for user in jsonData["users"]:
                if user["userID"] == uid:
                    tempID = 1
                    for event in user["events"]:
                        if(event["eventID"] > tempID):
                            tempID = event["eventID"]
                    eid = tempID+1
                    eventData.update( { "eventID" : eid } )
                    eventarray = user["events"]
                    eventarray.append(eventData)
                    user["events"] = eventarray
                    file.seek(0)
                    json.dump(jsonData,file,indent=4)

def deleteEvent(uid, eid):
    #
    # Finds event with eid under the user 
    # and deletes it 
    #
    #
    with open('events.json','r+') as file:
        jsonData = json.load(file)
        
        #has the user created events yet?
        if not any(user["userID"]==uid for user in jsonData["users"]):
            print("You have yet to create an event")
            return False
        # does the user have any events not deleted
        if any(user["userID"]==uid and user["events"]==[] for user in jsonData["users"]):
            print("You have no events to delete")
            return False
        
        found = False
        # only at this point if valid deletion targets exist
        #each user's full 'profile'
        for user in jsonData["users"]:
            #only the correct user
            if user["userID"]==uid: 
                for i in range(len(user["events"])):
                    if user["events"][i]["eventID"]==eid:
                        user["events"].pop(i)
                        found = True
                        break
    with open('events.json','w') as file:
        json.dump(jsonData,file,indent=4)
        return found

def signup(uname, pword):

    #
    # Opens logins file
    #   loads data
    #   checks for any usernames shared with the parameter username
    #   if doesnt exist, creates a new user
    #   if it does, tells you it already exists and optionally reroutes to login
    #

    with open('logins.json', 'r+') as file:
        jsonData = json.load(file)
        check = any(login["username"]==uname for login in jsonData["users"])
        if not check:
            for userID in jsonData["users"]:
                maxID = 0
                if(userID["userID"] > maxID):
                    maxID = userID["userID"]
            uid = maxID+1
            signupData = {
                "userID":uid,
                "username":uname, 
                "password":pword
                }
            jsonData["users"].append(signupData)
            file.seek(0)
            json.dump(jsonData,file,indent=4)
            print("Signed in")
            for id in jsonData["users"]:
                if(id["username"] == uname):
                    return id["userID"]
    print("Username taken, if you are loggin in, please use login")
    input1 = input("Would you like to login instead?(y/n): ")
    if input1 == "y":
        return loginButton()
    else:
        return signupButton()

def login(uname, pword):

    #
    # Opens logins file
    #   loads data
    #   checks for users with both uname and pword
    #   if they exist, print logged in and return their ID
    #   if they dont, print incorrect username or password, and allow relogin
    #

    with open('logins.json', 'r') as file:
        jsonData = json.load(file)
        check = any((login["username"]==uname and login["password"]==pword) for login in jsonData["users"])

        # Username and password exist together
        if check:
            print("Logged In")
            for id in jsonData["users"]:
                if(id["username"] == uname):
                    return id["userID"]

        # Username and password do not exist together
        else:
            print("Username or Password incorrect")
            print("Please try again")
            return loginButton()
            

def hash(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def signupButton():
    # send to page that lets you enter this information
    print("\nSign Up")
    username = hash(input("Enter Username: "))
    password = hash(input("Enter Password: "))
    return signup(username, password)

def loginButton():
    # send to page that lets you enter this information
    print("\nLog In")
    username = hash(input("Enter Username: "))
    password = hash(input("Enter Password: "))
    return login(username, password)

def createEventButton(uid):
    # send to page that lets you create event
    print("\nEvent Creation")
    name = input("Enter the name of the event: ")
    day = input("Enter the day of the event: ")
    time = input("Enter the time of the event: ")
    duration = input("Enter the duration of the event: ")
    description = input("Enter the description of the event: ")
    createEvent(uid, name, day, time, duration, description)

def deleteEventButton(uid):
    # will be on the page when viewing event and eid will already be known
    print("\nEvent Deletion")
    eid = int(input("What is the id of the event you want deleted: "))
    if(deleteEvent(uid, eid)):
        print("Event deleted successfully")
    else:
        print("Event deletion failed")

def viewEventButton(uid):
    # Essentially "on click of event" button with the info of the specific event
    print("\nWhich event would you like to view?")
    eid = int(input("What is the id of the event you want to view: "))
    if(viewEvent(uid,eid)==False):
        print("Event ID does not exist\n")