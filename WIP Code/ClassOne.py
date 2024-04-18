#ClassOne.py
class Calculator(object):
    #define class to simulate a simple calculator
    def __init__ (self):
        #start with zero
        self.__current = 0

    def add(self, amount):
        #add number to current
        self.__current += amount

    def getCurrent(self):
        return self.__current

    def testFuncCall(self):
        self.__testFunction()

    def __testFunction(self):
        print("This is a test")