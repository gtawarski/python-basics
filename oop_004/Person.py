import datetime

class Person:
    def __init__(self, firstName, lastName, dateOfBirth):
        self.FirstName = firstName
        self.LastName = lastName
        self.DateOfBirth = dateOfBirth
        
    def about(self):
        return self.FirstName + " " + self.LastName + " was born on " + self.DateOfBirth.strftime("%m/%d/%Y")