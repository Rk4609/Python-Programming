from random import randint
# 1. Create a class “Programmer” for storing information of few programmers working at
# Microsoft.

class Programmer:
    company="Microsoft"

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p = Programmer("Rakesh",490000,306703)
print(p.name,p.salary,p.pin,p.company)

p = Programmer("Sachin",100000,306703)
print(p.name,p.salary,p.pin,p.company)
        
#=========================================================================================
# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"the square is {self.n * self.n}")

    def cube(self):
        print(f"the cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")
    

r = Calculator(4)
r.square()
r.cube()
r.squareroot()

#===================================================================================================
# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using
# ‘object.a = 0’. Does this change the class attribute?

class demo:
    a= 4

o = demo()
print(o.a)  #prints the class attributes because instance attributes is not present

o.a=8  #instance attributes is set
print(o.a)   ##prints the instance attributes because instance attributes is  present

print(demo.a) # Prints the class attributes

#===================================================================================================
# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"the square is {self.n * self.n}")

    def cube(self):
        print(f"the cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")
    
    @staticmethod
    def hello():
        print("Hello Calculator...")

r = Calculator(4)
r.hello()
r.square()
r.cube()
r.squareroot()

#===================================================================================================
# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get
# fare information of train running under Indian Railways.

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book( self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Ticket no :{self.trainNo} is running on the time ")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222,5999)}")

t = Train(12233)
t.book("Jaipur","delhi") 
t.getStatus()
t.getFare("Jaipur","Delhi")

#===================================================================================================
# 6. Can you change the self-parameter inside a class to something else (say “harry”)? Try
# changing self to “slf” or “harry” and see the effects.


class Train:
    def __init__(slf,trainNo):  #self==slf
        slf.trainNo = trainNo
        print("Welcome to Aravali Express...")

    def book( self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Ticket no :{self.trainNo} is running on the time ")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222,5999)}")

t = Train(12233)
t.book("Jaipur","delhi") 
t.getStatus()
t.getFare("Jaipur","Delhi")

