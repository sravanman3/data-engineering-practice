#Sample Print
print("Hello World!")

#Printing Shapes
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")


#Variables
char_name = "Mike"
char_age = "30"

print("His name is "+char_name+",")
print("He is " + char_age + ".")

char_name="Jacob"
char_age = 35
print("He like his name: "+ char_name +" ,")
print("But he doesnt like to be "+ str(char_age) +".")


#Working with Strings:
phrase = "Giraffe Academy"

print(phrase.upper())
print(phrase.lower())
print(phrase.islower())
print(phrase.isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("c"))
print(phrase.index("Acad"))
print(phrase.replace("Giraffe","Elephant"))

##Working with Numbers
num1 = input("Enter a Number: ")
num2 = input("Enter another Number: ")

result = num1 + num2 ##this will give the value are string as by default the input is treated as string

print(result)

result = int(num1) + int(num2) ## integer
print(result)
result = float(num1) + float(num2) ## float
print(result)


from math import *

print(2 + 3)
print(2 + 3 * 4) #14
print((2+3) * 4) #20 BODMAS

print(abs(-3))
print(pow(4,2))
print(max(4,6))
print(min(3,1))
print(round(3.4))

print(floor(3.4))
print(ceil(3.4))
print(sqrt(25))


## Getting inputs from users:
name  = input("Enter your name: ")
age = input("Enter your age: ")


print(age.isnumeric())
print("Name is: "+ name + " and age is :"+age+".")

##Basic Calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2 # treated as string

print(result)

# result = int(num1) + int(num2)
# print(result)

result = float(num1) + float(num2)
print(result)

result = float(num1) + int(num2)
print(result)