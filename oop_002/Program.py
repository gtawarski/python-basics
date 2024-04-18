import datetime
import Person

myPerson = Person.Person('Gregory', 'Awarski', datetime.datetime(1980, 2, 8))

print(myPerson.FirstName + " " + myPerson.LastName + " was born on " + myPerson.DateOfBirth.strftime("%m/%d/%Y"))