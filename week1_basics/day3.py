# tuples -- Immutable - cant be changed/modified once created

coordinates = (2,3)
print(coordinates[1])


# #Functions

def say_hi(name,age):
    print(f"Hello {name}, you are {age} years old. " + "\njust testing conversion " + str(age))

say_hi("Alex",19)
###############################
def cube_cal(num1):
    return pow(num1,3)

print(cube_cal(3))


# #IF Statements
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not is_tall:
    print("You are male but not tall")
elif not is_male and is_tall:
    print("You are not male but tall")
else:
    print("You are neither male not tall")

if is_male or is_tall:
    print("You are either male or tall or both")
else:
    print("You are neither male nor tall")

# #IF - Comparison Operators
def max_num(num1, num2, num3):
    if num1 >= num2 and num1>=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(10,20,30))
print(max_num(10,200,30))
print(max_num(100,20,30))

# #Function to find max numbers from input
def max_num_5(n1,n2,n3,n4,n5):
    max_n = n1
    for i in n1,n2,n3,n4,n5:
        print(f"i: {max_n}")
        if max_n <=i:
            max_n = i

    return max_n

print(max_num_5(1000,80,300,40,50))


# #Better Calculator
def calci(num1, num2,op):
    num1 = float(num1)
    num2 = float(num2)
    if op == "+":
        return num1 + num2
    elif op == '-':
        return num1-num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Please enter a valid Operator"

print(calci(10,4,")"))
