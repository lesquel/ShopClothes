from .Person import Person

class Costumer(Person):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)   