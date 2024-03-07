a = 33
b = 200
if  b > a:
    print(f"b {b} is greater that a {a}")

if a > b:
    print(f"Value a {a} is greater thant value of b {b}")
else:
    print(f"Value a {b} is greater thant value of b {a}")

a = 10
b = 5
c = 20
if a > b:
    print(a)
elif b > a:
    print(b)
elif b > c:
    print(c)
elif a > c:
    print(c)
print("\n")

##logical and operator
if a > b  and c > a:
    print(f"The value of a : {a} is greater than value of b {b} value of c : {c} is greater than  value of a : {a}" )
else:
    print("Wrong again try again")
##logical or operator
if c > 20 or b < 20:
    print("Once conditions is true")

print("\n\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
colors = ["red", "blue", "purple"]
for x in colors:
    for y in fruits:
        print(x,y)