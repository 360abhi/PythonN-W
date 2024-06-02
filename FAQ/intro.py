
# Raising a custom exeption
class CustomError(Exception):
    pass

def risk():
    raise CustomError("You have tapped into a risky function")

try:
    risk()
except CustomError as e:
    print(str(e))

# Random moddule import

from random import *

for i in range(5):
    print(randint(1,10))

# Unlike the range function the randint function includes both the 

# None type : every function returns None if it doesnt return anything

spam = print("Hello")
print(spam == None)

# Local and global scope

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 19
    eggs = 17

spam()

# the eggs of bacon are destroyed after its scope is over so eggs still
# have the values from the spam function

