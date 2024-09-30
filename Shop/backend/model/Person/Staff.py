from .Person import Person
class Staff(Person):
    def __init__(self, id: int, username: str, password: str, name: str):
        super().__init__(id, username, password)        