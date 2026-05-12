class Employee:
    salary=49000   
    language="python"

    def getInfo(self):
        print(f"The language is {self.language}.and the salary is {self.salary}")
        
    @staticmethod
    def greet():  #dont pass ne self usinf staticmehod
        print("Happy ending")
    
rk = Employee()   
# rk.language="javascript"  
# print( rk.name ,rk.language, rk.salary)

rk.getInfo()
rk.greet()
# Employee.getInfo(rk)