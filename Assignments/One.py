from functools import reduce
from itertools import count

#
# #TOPIC: Python Basics Variable
#
#
# #1. Declare two variables, `x` and `y`, and assign them integer values. Swap the values of these variables without using
# # any temporary variable
#
# x = 10
# y = 20
# y,x = x,y
#
# print(f'x = {x}, y = {y}')
#
#
# """
# 2. Create a program that calculates the area of a rectangle.
# Take the length and width as inputs from the user and store them in variables.
# Calculate and display the area
# """
#
# def calcAreaOfRectangle(l,b):
#     return l*b
#
# print(calcAreaOfRectangle(10,20))
#
#
# """
# 3. Write a Python program that converts temperatures from Celsius to Fahrenheit.
# Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit, and display the result.
# """
#
# def convertCelsiusToFahrenheit(temperatureInCelsius):
#
#     return (temperatureInCelsius * 9/5) + 32
#
# fahrenheit = str(convertCelsiusToFahrenheit(10)) + '°F'
# print(fahrenheit)
#
#
# #TOPIC: String Based Questions
#
# #1. Write a Python program that takes a string as input and prints the length of the string.
#
# myString = str(input('enter string = '))
#
# myStringLen = len(myString)
#
# print(myStringLen)
#
# #2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.
#
# sentence = str(input('enter sentence = ')).lower()
#
# vowelsList = 'aeiou'
#
# Method 1
# c = 0
# for l in sentence:
#     for v in vowelsList:
#         if v == l:
#             c += 1
#             break
#
# print(c)
#
# Method 2
# cnt = len(list(filter(lambda l : l in vowelsList ,sentence)))
#
# print(cnt)

# 3. Given a string, reverse the order of characters using string slicing and print the reversed string.

# myString = 'pythonskills'
#
# print(f'Reverse of {myString} is {myString[::-1]}')


# 4. Write a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).
# myString = str(input('Enter the String here = '))
# reverseString = myString[::-1]
#
# if myString == reverseString:
#     print(f'{myString} is Palindrome')
# else:
#     print(f'{myString} is not a Palindrome')


# 5. Create a program that takes a string as input and removes all the spaces from it.
# Print the modified string without spaces.

myString = str(input('Enter the String here = '))

stringWithoutSpaces = str(reduce(lambda x, y: x + y, list(filter(lambda s: s != ' ', myString))))

print(stringWithoutSpaces)
