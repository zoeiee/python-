#how do you print a function
print("Hello World")

#how do you create a variable and its name
message = "Hello sweetie wassup, do you need some cofi?"
print(message)


#how do you tackle single quotes dilemma
oh = 'Bobby\'s World'
oh = "Bobby's World"

#how do you print length of your string
sentence = "Hey Aditi wassup, how's the world going"
print(len(sentence))

#how do you print the number of characters in your string 

#how do you do slicing of your string and when does it show error
example = "Hey Agatha"
print(example[:6])


#how do you make everything uppercase/lowercase
print(example.lower())
print(example.upper())

#how do you count the number of times a letter or word in a string repeats
print(message.count('Hey'))
print(message.count('a'))

#how do you find a word in your string and when does it show negative
print(example.find('Agatha'))
print(message.find('Agatha'))

#how do you replace characters in your string
candy = "my fav chocolate is cadbury"
candy = candy.replace("cadbury", "kitkat")
print(candy)

#how do you concatenate variables
greeting = "Hello"
name = "Stacy"
sign = greeting + ', ' + name
print(sign)

#what are formatted strings
xyz = "Hellow"
abc = "Aditi"
final = "{}, {}. Welcome!" .format(xyz, abc)
print(final)
