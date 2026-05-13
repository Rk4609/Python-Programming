class Employee:
    # company="TATA"
    name="Sachin"
    salary =35000
    def show(self):
        print(f"The employee name is {self.name} and the salary is {self.salary}")

class Coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language : {self.language}")


class Programmer(Employee,Coder):   # inherit for Employee class
    company="HCL"
    def showLanguage(self):
        print(f"The name is company {self.company} and he is a good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()



