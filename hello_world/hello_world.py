from other import *

# main function
def main():
    print('Hello, world')
    print('This is my demo.  Isn\'t it great?')
    print(myTest())
    print(generate_random_number())
    print('Test')
    
# number test function
def myTest() -> int:
    num1: int = random.randint(1, 100)
    num2: int = random.randint(1, 100)
    
    print (num1)
    print (num2)
        
    return num1 + num2
    
main()