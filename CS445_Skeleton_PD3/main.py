from func import *
print("Welcome to Weekly Planner")
print("What would you like to do?")
print("(Sign up) or (Log in)")
task = input("->").lower()

while(True):
    if task == "sign up":
        uid = signupButton()
        break
    elif task == "log in":
        uid = loginButton()
        break
    else:
        print("Not an option, please try again")
        task = input("->").lower()

while(True):
    print("Would you like to create an event, delete an event, or view all events?")
    print("(Create) (Delete) (View All) (View One) (Exit)")
    task = input("->").lower()
    if task == "create":
        createEventButton(uid)
    elif task == "delete":
        deleteEventButton(uid)
    elif task == "view all":
        viewAllEvents(uid)
    elif task == "view one":
        viewEventButton(uid)
    elif task == "exit":
        break
    else:
        print("Not an option, please try again")

print("Success?")