from .Person import Person
class Staff(Person):
    def __init__(self, username: str, password):
        super().__init__(username, password)        