"""name = input("Enter your name: ")
print("Hello", name)
s = "angelie"
t = 56
print(s, t)

x, y = input("Enter two values for x and y: ").split()
print("The number of girls is: ", x)
print("The number of boys is: ", y)

n = int(input("How many roses? "))
print("The number of roses are: ", n)

a = 89
b = 7.45
print(type(b))

r = 56
print(type(r))
float_r = float(r)
print(type(float_r))

x = 5
y = x
x = 6
print(x,y)
a = 23
b = 5
print("addition: ", a + b)

print("subtraction: ", a - b)
print("multiplication: ", a * b)
print("division: ", a / b)
print("floor division: ", a // b)
print("modulus: ", a % b)
print("exponential: ", a ** b)

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

a = True
b = False
print(a and b)
print(a or b)
print(not a)

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


a = 45
b = 87
list = [23, 43, 87, 32]
if (a not in list):
    print("MIAUUUU")
else:
    print("HEEHEHEH")
if(b not in list):
    print("oops")
else: 
    print("yayaya")

a, b = 45, 34
min = a if a<b else b
print(b)

n = 4
for i in range(0,n-1):
    print(i)
li = ["My", "name", "is", "Agent 091"]
for i in li:
    print(i)
tup = ("My", "name", "is", "Agent 091")
for i in tup:
    print(i)
s = "abc"
for i in s:
    print(i)
d = dict({'x': 1, 'y': 2, 'z': 3})
for i in d:
    print(i)
set1 = {1, 2, 3, 4}
for i in set1:
    print(i)

li = ["My", "name", "is", "Agent 091"]
for index in range(len(li)):
    print(li[index])

cnt = 0
while(cnt < 5):
    cnt += 1
    print("Hello, Codeforces!")

for i in range(1,5):
    for j in range(i):
        print
def fun():
    print("Hello, Codeforces!")

fun()
fun()
fun()
fun()

def func(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
print(func(56))
print(func(33))"""

s = "Final Python Docs"
print(s)
for char in s:
    print(char)
