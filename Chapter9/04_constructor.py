#Example--1
class Employee:
    salary=49000   
    language="python"

    def __init__(self):   # constructor  --- dunder method called automatically
        print(" I am creating an object...")

    def getInfo(self):
        print(f"The language is {self.language}.and the salary is {self.salary}")
        
    @staticmethod
    def greet():  #dont pass ne self usinf staticmehod
        print("Happy ending")
    
rk = Employee()   
print(rk.language,rk.salary)
sb=Employee()


#Eample--2

class Employee:
    salary=49000   
    language="python"

    def __init__(self,name,salary,language,age):   # constructor  --- dunder method called automatically
        self.name=name
        self.salary=salary
        self.language=language
        self.age=age
        print("I am creating an object...")

    def getInfo(self):
        print(f"The language is {self.language}.and the salary is {self.salary}")
        
    @staticmethod
    def greet():  #dont pass ne self usinf staticmehod
        print("Happy ending")
    
rk = Employee("Rakesh",49000,"Python",22)    #object in passing value for constuctor
print(rk.name,rk.salary,rk.language,rk.age)



