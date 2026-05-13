a = int(input("Enter a number :"))
b = int(input("Enter b number :"))
 
if(b == 0):   #zeroDivision Error in python a/b  10/0
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero ")
else:
    print(f"The divison is a/b is {a/b}")