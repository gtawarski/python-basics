from datetime import datetime
from Person import Person

myPerson = []
myPerson.append(Person('Gregory', 'Awarski', datetime(1980, 2, 8)))
myPerson.append(Person('John', 'Doe', datetime(1970, 3, 15)))
myPerson.append(Person('Jane', 'Smith', datetime(1960, 4, 20)))
myPerson.append(Person('Bob', 'Johnson', datetime(1960, 4, 17)))

for thisPerson in myPerson:
    print(thisPerson.about() + " and is " + str(thisPerson.age()) + " years old.")