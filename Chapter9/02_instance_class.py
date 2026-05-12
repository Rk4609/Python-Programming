
class Employee:
    salary=49000   # this is a class attributes
    language="python"
    
rk = Employee()   #object create
rk.language="javascipt"  # this is a instance attributes   --
#  Instance attributes take preference over class attributes during assignment & retrieval
print(rk.language, rk.salary)