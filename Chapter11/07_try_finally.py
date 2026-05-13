try:
    a =int(input("enter a number :"))
    print(a)

except Exception as e:
    print(e)

finally:  #final block always run because condi true or false
    print("I am inside")


#------------------------------
def main():
    try:
        a =int(input("enter a number :"))
        print(a)
        return

    except Exception as e:
         print(e)
         return
  
    finally:  #final block always run because condi true or false
        print("I am inside")

main()