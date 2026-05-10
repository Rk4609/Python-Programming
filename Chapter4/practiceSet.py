# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
words={
    "madad":"help",
    "namste":"hello",
    "kursi":"chair",
    "billi":"cat"
}

word = input("Enter a word you want to meaning :")
print(words[word]) # word key values  madad=help


# 2. Write a program to input eight numbers from the user and display all the unique numbers
# (once).
s=set()
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
print(s)  # unique number={1, 2, 3, 4, 6, 8}

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# answer --# yes we have a set with 18 (int) and '18' (str) # add in set

s= set()
s.add(18) #int
s.add("18") #str
print(s)  # {18, '18'}

# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))  #length is 2 because 1==1.0 is true 20=20.0

# 5. s = {}
# What is the type of 's'?s
s={}
print(type(s)) # dict class

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.
s={}
name=input("Enter friend name :")
lang = input("Enter language name :")
s.update({name:lang})
name=input("Enter friend name :")
lang = input("Enter language name :")
s.update({name:lang})
name=input("Enter friend name :")
lang = input("Enter language name :")
s.update({name:lang})
name=input("Enter friend name :")
lang = input("Enter language name :")
s.update({name:lang})
print(s)
# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# update the value in program 6 value same

# 8. If languages of two friends are same; what will happen to the program in problem 6?
# key same

# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

# nothing will change