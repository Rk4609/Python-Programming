from functools import reduce
# 1. Create two virtual environments, install few packages in the first one. How do you create
# a similar environment in the second one?
# Pending ----- env1 and env2 in install packages

# 2. Write a program to input name, marks and phone number of a student and format it using
# the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name =input("Enter a name :")
marks = int(input("Enter a marks :"))
phone = int(input("Enter a Number :"))
d = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone)
print(d)


# 3. A list contains the multiplication table of 7. Write a program to convert it to vertical string
# of same numbers.
# 7
# 14
# .
# .
# .

table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(s)

# 4. Write a program to filter a list of numbers which are divisible by 5.

l = [5,29,40,25,85,38,22,1]

def num(n):
    if(n%5 == 0):
        return True
    return False
divide = filter(num,l)
print(list(divide))



# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
# l = [5,293,40,25,85,999,38,22,1]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar
# virtualenv.


# Pending----

# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.run()