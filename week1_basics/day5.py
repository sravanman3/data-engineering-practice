# Exponent Function

def raise_to_power(base_num,power_num):
    result = 1
    for i in range(power_num):
        result = result * base_num

    return result

print(raise_to_power(3,5))

# # 2D List and Nested Loops:
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(numbers[2][2])

for row in numbers:
    for col in row:
        print(col)


##Translator:
def translate_phrase(phrase):
    translated_phrase = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translated_phrase = translated_phrase + "G"
            else:
                translated_phrase = translated_phrase + "g"
        else:
            translated_phrase = translated_phrase + letter
    return translated_phrase


print(translate_phrase("Only Doctor"))


# # Try Except
try:
    num1 = int(input("Enter a number: "))
    print(num1)
    ans = 10/num1
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)

