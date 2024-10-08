from .person import Person
class Staff(Person):
    def __init__(self, username: str, password):
        super().__init__(username, password)        
    
    def __str__(self):
        return f"Staff: {self.username}"