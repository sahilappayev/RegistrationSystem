class User:

    def __init__(self, userno, name, surname, age, username, password):
        self.__userno = userno
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__username = username
        self.__password = password

    def set_user_no(self, userno):
        self.__userno = userno

    def get_user_no(self):
        return self.__userno

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_surname(self, surname):
        self.__surname = surname

    def get_surname(self):
        return self.__surname

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password
