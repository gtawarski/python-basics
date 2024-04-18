import datetime
import Person

myPerson = []
myPerson.append(Person.Person('Gregory', 'Awarski', datetime.datetime(1980, 2, 8)))
myPerson.append(Person.Person('John', 'Doe', datetime.datetime(1970, 3, 15)))
myPerson.append(Person.Person('Jane', 'Smith', datetime.datetime(1960, 4, 20)))

for thisPerson in myPerson:
    print(thisPerson.about())