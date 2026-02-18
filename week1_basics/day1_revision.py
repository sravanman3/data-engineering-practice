print("Good Day!")

print("|------|")
print("|      |")
print("|      |")
print("|      |")
print("|______|")

char_name = "Adam"
char_age = "34"

print("Name is "+char_name+" and age is "+char_age+".")
print(f"Name is {char_name} and age is {char_age}")

phrase = "Lenskart Glasses"

print(phrase.lower())
print(phrase.upper())
print(phrase[3])
print(len(phrase))
print(phrase.find("z"))
print(phrase.replace("kart","mart"))
print(type(phrase))

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2 #string concat
print(result)
result = int(num1) + int(num2)
print(result)

result = float(num1) + float(num2)
print(result)


num = -3.4

print(abs(num))
print(round(abs(num)))

a = 2
print(min(8,2))
print(max(3,9))
print(pow(4,a))

import math as m
#from math import *

print(m.floor(2.3))
print(m.ceil(2.4))
print(m.sqrt(10))

