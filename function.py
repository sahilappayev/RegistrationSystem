from lib import User
from db import users
import db


# Input functions

def textInput(arg):
    i = input(f"Enter {arg}: ").strip()
    if len(i) == 0:
        print(f"The {arg} cannot be empty!")
    else:
        return i


def numberInput(arg):
    number = input(f"Enter {arg}: ").strip()
    if len(number) == 0:
        print(f"{arg.capitalize()} cannot be empty!")
    else:
        if number.isdigit():
            return int(number)
        else:
            print("Wrong input!")


def inputUserno():
    userno = numberInput("user number (consist 3 digits)")

    if userno < 100 and userno > 999:
        print("User number not entered correctly!")
        userno = None
    else:
        for user in db.readDb():
            if user["userno"] == userno:
                print("There is user in the system by this user number. Try another user number.")
                userno = None
    return userno


# Main functions

def addUser():
    userno = inputUserno()

    name = None
    if userno:
        name = textInput("name").capitalize()

    surname = None
    if name:
        surname = textInput("surname").capitalize()

    age = None
    if surname:
        age = numberInput("age")

    username = None
    if age:
        username = textInput("username")
    password = None
    if username:
        password = textInput("password")
    if userno and name and surname and age and username and password:
        obj = User(userno, name, surname, age, username, password)
        db.addUserToDb(obj)


def printUserJson(json):
    print(f"""
            User number: {json["userno"]}
            Name: {json["name"]}
            Surname: {json["surname"]}
            Age: {json["age"]}
            Username: {json["username"]}
            Password: {json["password"]}
        """)


def showAllUsers():
    if len(db.readDb()) == 0:
        print("There is no user in the system!")
    else:
        for user in db.readDb():
            printUserJson(user)


def showUserByName(username):
    ceck = False

    for user in db.readDb():
        if str(user["username"]).lower() == username.lower():
            ceck = True

    if ceck:
        for user in db.readDb():
            if str(user["username"]).lower() == username.lower():
                printUserJson(user)
    else:
        print(f"Not found user by '{username}' username in system")


def findUserByUserNo(userno):
    ceck = False

    for user in db.readDb():
        if user["userno"] == userno:
            ceck = True

    if ceck:
        for user in db.readDb():
            if user["userno"] == userno:
                return user
    else:
        print(f"Not found user by {userno} user number in the system.")
        None


def showUserByUsernoWithInput():
    if len(db.readDb()) == 0:
        print("There is no user in the system!")
    else:
        userno = numberInput("user number (consist 3 digits)")
        userJson = findUserByUserNo(userno)
        if userJson:
            printUserJson(userJson)


def deleteUser():
    if len(db.readDb()) == 0:
        print("There is no user in the system!")
    else:
        userno = numberInput("user number (consist 3 digits)")
        userJson = findUserByUserNo(userno)
        if userJson:
            db.deleteUserFromDb(userJson)
            print(f"User {userJson['name']} wihth {userno} user number deleted succesfuly!")


def showTheLongestUsername():
    if len(db.readDb()) == 0:
        print("There is no user in the system!")
    else:
        longestUsername = ""
        for user in db.readDb():
            if len(user["username"]) > len(longestUsername):
                longestUsername = user["username"]

        showUserByName(longestUsername)


def showTheLongThan8PassUser():
    if len(db.readDb()) == 0:
        print("There is no user in the system!")
    else:
        for user in db.readDb():
            check = True
            if len(user["password"]) > 8:
                check = False
                printUserJson(user)
            elif check:
                print("There is no user in the system with password length more than eight!")


# Menu functions

def menu():
    menu = input("""
    _______________________________________________________________________________________
        1. Add user
        2. Show all users
        3. Show user by user no
        4. Show user who has the longest username
        5. Shwo users whom password length more than eight
        6. Delete user by user no
        7. Exit
    _______________________________________________________________________________________
    """).strip()
    if menu.isdigit() and 0 < int(menu) < 8:
        return int(menu)
    else:
        print("Wrong input!")


def showMenu():
    m = menu()
    if m == 1:
        addUser()
    elif m == 2:
        showAllUsers()
    elif m == 3:
        showUserByUsernoWithInput()
    elif m == 4:
        showTheLongestUsername()
    elif m == 5:
        showTheLongThan8PassUser()
    elif m == 6:
        deleteUser()
    elif m == 7:
        exit()
