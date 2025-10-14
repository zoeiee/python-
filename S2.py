#printing type of variables 
num = 4.14
print(type(num))

#arithmetic operators
#addition
print(3 + 2)

#subtraction
print(3 - 2)

#multiplication 
print(3 * 2)

#division
print(3 / 2)

#floor division 
print(3 // 2)

#exponent
print(3 ** 2)

#modulus
print(3 % 2)

#precedence via paranthesis
#case1: here it will go from left to right in an order since no paranthesis is used
print(3 * 2 + 1)

#here paranthesis decides which operation to do first- marks exclusivity
print(3 * (2 + 1))

#incrementing
num = 1
num += 1
print(num)

#using absolute values
print(abs(-3))

#rounding values
print(round(3.78))
#specifying the decimal values upto which the rounding is needed
print(round(3.56, 1))

#comparisons 
#equal

num1 = 3
num2 = 2
print(num1 == num2)

#not equal
print(num1 != num2)

#greater than
print(num1 > num2)

#less than
print(num1 < num2)

#greater or equal
print(num1 >= num2)

#less or equal
print(num1 <= num2)

#casting:converting strings to integers
num_1 = '100'
num_2 = '200'
print(num_1 +  num_2) #no 
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 +  num_2) #yes


