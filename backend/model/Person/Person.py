from abc import ABC,abstractmethod
class Person(ABC):
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


    def authenticate(self, password: str):
        return self.__password == password

    def change_password(self, old_password: str, new_password: str):
        if self.authenticate(old_password):
            self.__password = new_password
            return True 
        return False

    def __eq__(self, other):
        return self.__username == other.__username 

    @abstractmethod
    def __str__(self):
        pass