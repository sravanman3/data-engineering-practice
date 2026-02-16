# data = {
#     "x": 10,
#     "y": 20,
#     "z": 10,
#     "p": 30,
#     "q": 20
# }
#
# reverse_dict = {}
#
# for key,value in data.items():
#     if value not in reverse_dict:
#         reverse_dict[value] = [key]
#     else:
#         reverse_dict[value].append(key)
#
#
# print(reverse_dict)


# nums = [1, 2, 2, 3, 3, 3, 4]
#
# dict_of_num = {}

# {
#  1: [1, 4],
#  2: [2],
#  3: [3]
# }

# for num in nums:
#     if num not in dict_of_num:
#         dict_of_num[num] = 1
#     else:
#         dict_of_num[num] += 1
#
# reverse_dict = {}
# for key, value in dict_of_num.items():
#     if value in reverse_dict:
#         reverse_dict[value].append(key)
#     else:
#         reverse_dict[value] = [key]
#
# print(reverse_dict)

#
# words = ["apple", "bat", "ball", "cat", "banana"]
# dict_words = {}
# rev_dict_words = {}
# for word in words:
#     dict_words[word] = len(word)
#
# for key,value in dict_words.items():
#     if value not in rev_dict_words:
#         rev_dict_words[value] = [key]
#     else:
#         rev_dict_words[value].append(key)
# print(dict_words)
# print(rev_dict_words)

# words = ["apple", "bat", "ball", "cat", "banana"]
#
# rev_dict = {}
#
# for word in words:
#     length = len(word)
#     if length not in rev_dict:
#         rev_dict[length] = [word]
#     else:
#         rev_dict[length].append(word)
# print(rev_dict)

records = [
    {"name": "Alice", "dept": "IT"},
    {"name": "Bob", "dept": "HR"},
    {"name": "Charlie", "dept": "IT"},
    {"name": "David", "dept": "Finance"},
]

dept_dict = {}

for record in records:
    if record["dept"] not in dept_dict:
        dept_dict[record["dept"]] = [record["name"]]
    else:
        dept_dict[record["dept"]].append(record["name"])

print(dept_dict)




