import math
#FUNCTIONS DEFINITION
def greet():
    print("Hello World")

greet()# called the function

#FUNCTION ARGUMENTS
def greeting(fname,lname):
    print(f"Hi there {fname} {lname}\n")#recognized the spacing
    print("Welcome to Learning Python Programming Language")

greeting("Gard","Safari")

#ANOTHER WAY OF PRINTING VAR CONCATENATION
fname = "Patience"
mName = "Bahati"
print(fname + " " + mName + " is coming to Zetech University")

#sum function
def sum(num1,num2):
    sum = num1 + num2
    print(sum)

sum(num1=4, num2=10)
#sum(num1=10,12) return positional keyword argument

#pass
def future():
    pass#the pass value is used when 2 program later / prevents the execution of the code statement between the future
    
future()


#break used to exit loop
number = int(input("Enter any number : "))
def primeNumber(number):
    for i in range(number):
        print(f"Number : {i}")
        if i == 5:#when the value is 5 the program exits
            break
primeNumber(number)

print("\n")
userNames = ["Gard","Alson", "John", "Safari", "Rocket"]
print(f"the length of the list userNames is {len(userNames)}")
def student(arrayValues):
    i = 0
    while i < len(arrayValues):
        print(arrayValues[i])
        i+=1

student(userNames)
for i in range(5):
    if i == 3:
        continue
    print(i)
        # print(f"Value of i is {i} and arrayValue is {arrayValues[i]}")


#print value in string and in a list
def fun(*argv):
    for item in argv:
        print(item) 
    """
    print(argv)

    """
fun("gard","alson","safari")

name = "Jane"
age = 25

print("Hello, %s! You're %s years old." % (name, age))
def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s"% (key,value))

myFun(first="Gard", mid="Alson" , age="23", year=2000)

root = math.sqrt(4)
print(f"root of the number 4 is {root}")