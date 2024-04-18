import datetime
import Person

myPerson = Person.Person()
myPerson.FirstName = 'Gregory'
myPerson.LastName = 'Awarski'
myPerson.DateOfBirth = datetime.datetime(1980, 2, 8)

print(myPerson.FirstName + " " + myPerson.LastName + " was born on " + myPerson.DateOfBirth.strftime("%m/%d/%Y"))