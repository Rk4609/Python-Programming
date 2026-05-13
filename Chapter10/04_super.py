class Employee:
    def __init__(self):
        print("Constructor of Employee...")
    a=5

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer...")
    b=10

class Manager(Programmer):
    def __init__(self):
        super().__init__()   # super class means upper class programmer together run
        print("Constructor of Manager...")
    c=15
    
m = Manager()
print(m.a,m.b,m.c)