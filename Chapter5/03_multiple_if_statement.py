# if else elif ladder
age = int(input("Enter your age :"))

# if statment 1
if(age%2==0):
    print(" Age is even")
    #end of statement 1

# if statment 2
if(age >= 18):
    print("You are above the age of consent")
    print("Good for you")
elif(age<0):
    print("You are Entering an invalid nagetive age")
else:
    print("You are below the age of consent")
#end of statement 2

print("End of Program")