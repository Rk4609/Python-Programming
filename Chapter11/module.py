def myFun():
    print("hey this is module myFun")

def run():   #this code is running in main.py
    print("horse is running..")
run()

#this code running only this file 
if(__name__ == "__main__"):
    #if this code is directly executed by running the file its present in 
    print("We are running directly this code..")
    myFun()
    print(__name__)

