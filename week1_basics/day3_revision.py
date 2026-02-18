# # 1) Tuple
t1 = (1, 2, 3, "Name")

print(t1)
print(t1[2])
try:
    t1[2] = 4
except:
    print("Tuple is immutable")


# # 2) Function with Real Logic
def count_even(numbers):
    even_counter = 0

    for i in numbers:
        if i % 2 == 0:
            even_counter += 1
    return even_counter


print(count_even([1, 2, 3, 4, 6, 9, 10]))

# # 3)Finding max number: I am not sure how to handle nulls yet.
def find_max(numbers):
    if len(numbers) == 0:
        return "Invalid list"
    else:
        max_num = numbers[0]
        for i in numbers:
            if max_num <= i:
                max_num = i
    return max_num

print(find_max([1,3,6,4,5]))

# # 4) Calculator:
def calculator(n1, n2, operator):
    n1 = float(n1)
    n2 = float(n2)
    if n2 ==0 and (operator == "/" or operator == "%"):
        return "Division by zero"
    if operator == "+":
        return n1+n2
    elif operator == "-":
        return n1-n2
    elif operator == "*":
        return n1*n2
    elif operator == "/":
        return n1/n2
    elif operator == "%":
        return n1%n2
    else:
        return "Invalid Operator"

print(calculator(10,2,"%"))


# # 5) Boolean Logic Scenario
is_student = False
has_id = True

if is_student and has_id:
    print("Allowed Entry")
else:
    print("Not allowed")

# # Bonus:
def bonus_val(n1,n2,n3,n4,n5):
    l1 = [n1,n2,n3,n4,n5]
    max_num = l1[0]
    for i in l1:
        if max_num <= i:
            max_num = i
    print(f"max_num is {max_num}")

    even_counter = 0
    for i in l1:
        if i %2 ==0:
            even_counter += 1
    print(f"even_counter is {even_counter}")

bonus_val(2,100,6,804,3)