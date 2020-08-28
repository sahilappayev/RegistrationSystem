import json

users = []

def deleteUserFromDb(userJson):
    users = readDb()
    users.remove(userJson)
    writeDb(users)

def addUserToDb(user):
    userDict = {
        "userno":user.get_user_no(),
        "name": user.get_name(),
        "surname": user.get_surname(),
        "age": user.get_age(),
        "username": user.get_username(),
        "password": user.get_password()
    }
    users.append(userDict)
    writeDb(users)

def readDb():
    with open("database.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    return users

def writeDb(users):
    with open("database.json", "w", encoding="utf-8") as file:
        json.dump(users, file)