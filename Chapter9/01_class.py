class Employee:
    salary=49000   # this is a class attributes
    language="python"
    
rk = Employee()   #object create
rk.name="Rakesh"  # this is a instance attributes
print( rk.name ,rk.language, rk.salary)

sb = Employee()
sb.name="Sachin"
print( rk.name ,rk.language, rk.salary)