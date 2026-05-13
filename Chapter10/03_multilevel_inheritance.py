class Employee:
    a =5
    def intro(self):
        print("My name is rk And i am a employee...")

class Programmer(Employee):  # Programmer inherit Employee
    b=10
    def proIntro(self):
        print("My name is Programmer")

class Manager(Programmer):   #manager inherit Programmer
    c=15
    def manager(self):
        print("I am a Manager in company")


emp = Employee()          
# emp.intro()
# print(emp.a)

pro= Programmer()
# pro.proIntro()
# print(pro.b)

man= Manager()
man.manager()
pro.proIntro()
emp.intro()
print(emp.a,pro.b,man.c)


