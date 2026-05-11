#default argument

def goodDay(name,ending="Thank you"):   # default argument means you can not provide parameter value then automatically provide default value
    print(f"Good day, {name} ")
    print(ending)

goodDay("Rakesh")
goodDay("Sachin","thanks")

