from .Person import Person

class Costumer(Person):
    def __init__(self, id: int, username: str, password: str):
        super().__init__(id, username, password)   