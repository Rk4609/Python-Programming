from functools import reduce
#map function
l =[1,2,4,5,6,7,9]

square = lambda x : x*x

sqList = map(square,l)

print(list(sqList))   #[1, 4, 16, 25, 36, 49, 81]

#filter example
def even(n):
    if(n%2==0):
        return True
    return False

evenOnly = filter(even,l)
print(list(evenOnly))   #[2, 4, 6]

# reduce example
def sum(a,b):
    return a+b

mul = lambda x,y: x*y
print(reduce(sum,l))  #32 total number
print(reduce(mul,l))    # lambda with 15120
   




