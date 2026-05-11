# 1. Write a program using functions to find greatest of three numbers.
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a=20
b=3
c=10
print(greatest(a,b,c))



# 2. Write a python program using function to convert Celsius to Fahrenheit.
def f_to_c(f):
    return 5*(f-32)/9  #formula
 
f = int(input("Enter temprature in F :"))
c = f_to_c(f)
print(f"{round(c,2)}°C")


# 3. How do you prevent a python print() function to print a new line at the end.
print("a")
print("b")
print("c",end="") # newline avoid
print("d",end="")


# 4. Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1)=1
sum(2)=1 + 2
sum(3)=1 + 2 + 3
sum(4)=1 + 2 + 3 + 4
sum(5)=1 + 2 + 3 + 4 + 5

sum(n) = sum(n-1) + n

'''

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

n=int(input("Enter a number :"))
print(sum(n))


# 5. Write a python function to print first n lines of the following pattern.
# ***
# **
# *
# - for n = 3

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)


# 6. Write a python function which converts inches to cms.

def inch_to_cms(inch):
    return inch * 2.54 #formula of inch to cms
n = int(input("ENTER THE VALUE OF INCHES :"))
print(f"THE CORRESPONDING VALUE IN CMS IS : {inch_to_cms(n)}")

# 7. Write a python function to remove a given word from a list and strip it at the same time.

def rem(l,word):
    n=[]
    for item in l:
            if not(item==word):
                  n.append(item.strip(word))
    return n

l = ["Rakesh","Rohan","Sachin","an"]
print(rem(l,"an"))

# 8. Write a python function to print multiplication table of a given number

def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

multiply(5)