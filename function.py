from lib import User
from db import database


# Input functions

def textInput(arg):
    return input(f"Enter {arg}: ").strip()


def numberInput(arg):
    number = input(f"Enter {arg}: ").strip()
    if number.isdigit():
        return number
    else:
        print("Wrong input!")


# Main functions

def getDataFromUser():
    name = textInput("name")
    surname = textInput("surname")
    age = numberInput("age")
    username = textInput("username")
    password = textInput("password")
    return [name, surname, age, username, password]


def createUserObj():
    return User(*getDataFromUser())


def addUserToDb():
    database.append(createUserObj())


def showAllUsers():
    if len(database) == 0:
        print("There is no user in the system!")
    else:
        for user in database:
            user.printUserInfo()


def showUserByName(name):
    ceck = False

    for user in database:
        if str(user.name).lower() == name.lower():
            ceck = True

    if ceck:
        for user in database:
            if str(user.name).lower() == name.lower():
                user.printUserInfo()
    else:
        print(f"Not found user by {name} name in system")


def showUserByNameWithInput():
    if len(database) == 0:
        print("There is no user in the system!")
    else:
        name = textInput("name")
        showUserByName(name)


def login():
    print("Login page not implemented yet :)")


def showTheLongestNameUser():
    if len(database) == 0:
        print("There is no user in the system!")
    else:
        longestName = ""
        names = []
        for user in database:
            names.append(user.name)

        for name in names:
            if len(name) > len(longestName):
                longestName = name

        showUserByName(longestName)


def showTheLongThan8PassUser():
    if len(database) == 0:
        print("There is no user in the system!")
    else:
        longestPass = ""
        passes = []
        for user in database:
            passes.append(user.password)

        for password in passes:
            if len(password) > len(longestPass):
                longestPass = password

        for user in database:
            if user.password == longestPass:
                user.printUserInfo()


# Menu functions

def menu():
    menu = input("""
    _______________________________________________________________________________________
        1. Login
        2. Add user
        3. Show all users
        4. Show user by name
        5. Show user who has the longest name
        6. Shwo users whom password length more than eight
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
        login()
    elif m == 2:
        addUserToDb()
    elif m == 3:
        showAllUsers()
    elif m == 4:
        showUserByNameWithInput()
    elif m == 5:
        showTheLongestNameUser()
    elif m == 6:
        showTheLongThan8PassUser()
    elif m == 7:
        exit()
