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
print(func(33))

s = "Final Python Docs"
print(s)
for char in s:
    print(char)

s = "Final Python Docs"
s1 = "f" + s[1:]
s2 = s.replace("Python", "Java")
print(s1)
print(s2)
print(s.upper())
print(s.lower())


#question 1

#METHOD1
a = 6
b = 8
print(a+b)
#METHOD2
sum = a + b
print("Sum of a and b is: ", sum)
#METHOD3
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
sum = a + b
print("Sum of a and b is: ", sum)
#METHOD4
def add(x,y):
    return x + y

sum = add(5678423, 23445)
print("Sum is: ", sum)
#METHOD5
sum = lambda p, q: p + q
print("Sum is: ", sum(5,8))

#question 2

#METHOD1
a = 34
b = 89
print(max(a, b))

#METHOD2
print(a if a > b else b)

#METHOD3
if (a > b):
    print
else:
    print(b)

#METHOD4
list = [a, b]
list.sort()
print(list[-1])

#QUESTION3

#METHOD1
p = float(input("Enter the principal amount:"))
r = float(input("Enter the rate of interest:"))
t = int(input("Enter the time period in years:"))

amount = (p * r * t)/100
print("The amount is:", amount)

#METHOD2
def fun(p,t,r):
    return(p*r*t)/100
p,t,r = 8,9,4
res = fun(p,t,r)
print(res)

#METHOD3
si = lambda p,t,r: (p*t*r)/100
p,t,r = 8,6,8
res= si(p,t,r)

print(res)

#QUESTION4
#method1
import math
r = 9
area = math.pi * (r ** 2)
print(area)

#method2
import math
r = 9
area = math.pi * math.pow(r, 2)
print(area)"""

from math import sqrt
def Prime(n, i):
    if i == 1 or i == 2:
        return True
    if n % i == 0:
        return False
    return Prime(n, i-1)
n = 13
i = int(sqrt(n)+ 1)
print(Prime(n,i))

