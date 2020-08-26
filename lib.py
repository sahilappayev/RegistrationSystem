class User:

    def __init__(self, name, surname, age, username, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.username = username
        self.password = password

    def printUserInfo(self):
        print(f"""
            Name: {self.name}
            Surname: {self.surname}
            Age: {self.age}
            Username: {self.username}
            Password: {self.password}
        """)
