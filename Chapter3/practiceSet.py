# # 1. Write a program to store seven fruits in a list entered by the user.
fruits=[]
f1 = input("Enter fruit name :")
fruits.append(f1)
f2 = input("Enter fruit name :")
fruits.append(f2)
f3 = input("Enter fruit name :")
fruits.append(f3)
f4 = input("Enter fruit name :")
fruits.append(f4)
f5 = input("Enter fruit name :")
fruits.append(f5)
f6 = input("Enter fruit name :")
fruits.append(f6)
print(fruits)


# 2. Write a program to accept marks of 6 marks and display them in a sorted manner.
marks=[]
f1 = int(input("Enter Marks here :"))
marks.append(f1)
f2 = int(input("Enter Marks here :"))
marks.append(f2)
f3 = int(input("Enter Marks here :"))
marks.append(f3)
f4 = int(input("Enter Marks here :"))
marks.append(f4)
f5 = int(input("Enter Marks here :"))
marks.append(f5)
f6 = int(input("Enter Marks here :"))
marks.append(f6)

marks.sort()
print(marks)

# 3. Check that a tuple type cannot be changed in python.
# tuple is immutable

# a=(67,77,"Rakesh")
# a[2]="rk"

# 4. Write a program to sum a list with 4 numbers.
#sum is buit in function
list =[7,8,3,2]
print(sum(list))

# 5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)
a= a.count(0) # total zero in tuple
print(a)

