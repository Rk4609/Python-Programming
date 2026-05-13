# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class twoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is :{self.i}i + {self.j}j")
        
class threeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is : {self.i}i + {self.j}j + {self.k}k")

a = twoDVector(1,2)
a.show()
b=threeDVector(7,8,4)
b.show()


#===================================================================================================
# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’.
# Add a method ‘bark’ to class ‘Dog’.

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow bow...")

d = Dog()
d.bark()

#===================================================================================================
# 3. Create a class ‘Employee’ and add salary and increment properties to it. Write a method
# ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes
# the value of increment based on the salary.

class Employee:
    salary=199
    increment=25    

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100

e= Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement=400
print(e.increment)

#===================================================================================================
# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators
# ‘+’ and ‘*’ which adds and multiplies them.

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Operator overloading for +
    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    # Operator overloading for *
    def __mul__(self, other):
        real = (self.real * other.real) - (self.imag * other.imag)
        imag = (self.real * other.imag) + (self.imag * other.real)

        return Complex(real, imag)

    # For printing object nicely
    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = Complex(2, 3)
c2 = Complex(4, 5)

print("Complex 1 :", c1)
print("Complex 2 :", c2)

print("Addition :", c1 + c2)

print("Multiplication :", c1 * c2)



#===================================================================================================
# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator
# which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self,values):
        self.values= values 
    
    #  Operator overloading for +
    def __add__(self, other):
        result=[]

        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])

        return Vector(result)
        
    #  Operator overloading for *

    def __mul__(self, other):
        dot_product=0

        for i in range(len(self.values)):
            dot_product += self.values[i] * other.values[i]

        return dot_product
    
    def __str__(self):
        return str(self.values)

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Vector 1 :", v1)
print("Vector 2 :", v2)

print("Addition :", v1 + v2)

print("Dot Product :", v1 * v2)


#===================================================================================================
# 6. Write __str__() method to print the vector as follows:
# 7i + 8j + 10k
# Assume vector of dimension 3 for this problem.

class Vector:

    def __init__(self, values):
        self.values = values

    def __str__(self):

        result = ""

        for i in range(len(self.values)):

            if i == 0:
                result += f"{self.values[i]}i"

            elif i == 1:
                result += f" + {self.values[i]}j"

            elif i == 2:
                result += f" + {self.values[i]}k"

        return result


v = Vector([7, 8, 10])

print(v)


#===================================================================================================
# 7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.


class Vector:

    def __init__(self, values):
        self.values = values

    # __str__ method
    def __str__(self):
        return " + ".join(
            f"{self.values[i]}{'ijk'[i]}" for i in range(len(self.values))
        )

    # Override __len__()
    def __len__(self):
        return len(self.values)


v = Vector([7, 8, 10])

print("Vector :", v)

print("Dimension of Vector :", len(v))