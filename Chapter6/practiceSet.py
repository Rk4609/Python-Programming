# 1. Write a program to print multiplication table of a given number using for loop.

n= int(input("Enter the number :"))
for i in range(1,11):
    print(f"{n} X {i} = {n * i}")


# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul","Sanjay"]

for name in l:
    if(name.startswith("S")):
        print(f"hello {name}")

# 3. Attempt problem 1 using while loop.

n=int(input("Enter the number :"))
i=1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i+=1



# 4. Write a program to find whether a given number is prime or not.
n=int(input("Enter the number :"))
for i in range(2,n):
    if(n%i)==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")



# 5. Write a program to find the sum of first n natural numbers using while loop.
n=int(input("Enter the number :"))
i=1
sum=0
while(i<=n):
    sum += i
    i += 1
print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.
# 5 = 1x2x3x4x4x5  =120
n=int(input("Enter the number :"))
product =1
for i in range(1,n+1):
    product = product * i

print(f"The factorial of {n} is {product}")


# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n=int(input("Enter the number :"))
for i in range(1,n+1):  #1 to 3 n+1=n
    print(" " * (n-i), end="") # n-i = 3-1=2 3-2=1 3-3=0
    print("*" * (2*i-1),end="") # 2*i-1= 2*1-1=2-1=1, 2*2-1=3
    print("")


# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n=int(input("Enter the number :"))
for i in range(1,n+1):
    print("*"* i, end="") #i=1 i=2 i=3
    print("")


# 9. Write a program to print the following star pattern.
# * * *
# *   *     for n = 3
# * * *

n=int(input("Enter the number :"))
for i in range(1,n+1):
    if(i==1 or i==n):  # 1=1 and 1=3 then print star
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")   #(n-2) =1
        print("*",end="")
    print("")


# 10. Write a program to print multiplication table of n using for loops in reversed order

n=int(input("Enter the number :"))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")

