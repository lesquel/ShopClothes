class Person:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password


    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value):
        self.__username = value
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):        
        self.__password = value