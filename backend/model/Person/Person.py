class Person:
    def __init__(self, id: int, username: str, password: str):
        self.__id = id
        self.__username = username
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value   
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