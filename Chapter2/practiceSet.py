# 1. Write a python program to display a user entered name followed by Good Afternoon using
# input() function.

name= input("Enter your name :")
print(f"Good Afternoon {name}")

# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
 Dear <|Name|>,
 You are selected!
 <|Date|>
 '''
print(letter.replace("<|Name|>","Rakesh").replace("<|Date|>","08 May 2026"))


# 3. Write a program to detect double space in a string.
# -1 -- not double space
# find double space--10

name = "Hey rakesh  jangid"
print(name.find("  "))  

# 4. Replace the double space from problem 3 with single spaces.
# double space convert single space

name = "Hey rakesh  jangid "
print(name.replace("  "," ")) 

# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry,\n\t this python course is nice.\n Thanks!"
print(letter)

