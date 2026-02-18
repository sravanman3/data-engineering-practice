# # Challenge 1
def max_mark_dict():
    marks = {
        "Alice": 80,
        "Bob": 92,
        "Charlie": 78,
        "David": 92
    }

    l1 = []

    key_list = list(marks.keys())
    max_mark = marks[key_list[0]]

    for i in key_list:
        if max_mark <= marks[i]:
            max_mark = marks[i]

    for j in key_list:
        if max_mark == marks[j]:
            l1.append(j)

    return l1

print(max_mark_dict())


# # 2 — Word Frequency Counter
def word_count(sentence):
    words = sentence.split()
    dict_count = {}

    for i in words:
        count = 0
        for j in words:
            if i.lower() == j.lower():
                count += 1
        dict_count[i.lower()] = count

    return dict_count

print(word_count("apple apple banana mango Mango apple"))

# # 3 — Reverse Dictionary
data = {
    "a": 1,
    "b": 2,
    "c": 1
}

data_keys = list(data.keys())
data_values = list(data.values())

dict_val = {}


# 4 — Improved Guess Game
import random as rm

def guess_game():
    words = ["apple", "banana", "mango"]
    random_word = rm.choice(words)
    guess_word = ""
    counter = 0
    while random_word != guess_word:
        guess_word = input("Guess a word: ")
        counter += 1
        if guess_word == random_word:
            print(f"You win! attempt count: {counter}")
            return "Completed"
    return None

print(guess_game())


# # 5 — Number Classification

def classify_numbers(numbers):
    positive_counter = 0
    negative_counter = 0
    even_counter = 0
    odd_counter = 0
    zero_counter = 0
    ret_dict = {}

    for i in numbers:
        if i > 0:
            positive_counter += 1
        elif i < 0:
            negative_counter += 1
        else:
            zero_counter += 1

        if  i % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

    ret_dict["even"] = even_counter
    ret_dict["odd"] = odd_counter
    ret_dict["zero"] = zero_counter
    ret_dict["positive"] = positive_counter
    ret_dict["negative"] = negative_counter

    return ret_dict

print(classify_numbers([10, -5, 0, 8, -2, 3]))