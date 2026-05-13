#  Variable type hint
age: int = 25
# Function type hints
def greeting(name: str,age:int):
 return f"Hello, {name} and age {age}!"
# Usage
print(greeting("Alice",22))



#------------------
from typing import List, Tuple, Dict, Union
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)  #only value
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}  #key value
# Union type
identifier: Union[int, str] = "ID123" #intchar

print(numbers,type(numbers))