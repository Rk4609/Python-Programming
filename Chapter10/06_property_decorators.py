class Employee:
    a = 5
    @classmethod  
    def show(cls):
        print(f"the value is attribute :{cls.a}")
    
    @property # property ke use se method ko variable type me use kr sakte h e.name not e.name()
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45  

e.name = "Rakesh jangid"
print(e.fname,e.lname)

e.show()
