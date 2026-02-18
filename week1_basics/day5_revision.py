# # # 1) Custom Power function
#
# def power(base, exponent):
#     result = 1
#     if exponent == 0:
#         result = 1
#     elif exponent >0:
#         for i in range(exponent):
#             result = result * base
#     else:
#         temp = 1
#         for i in range(-1*exponent):
#             temp = temp * base
#         result = result/temp
#
#     return result
#
#
# print(power(2,-3))
# print(pow(2,-3))


# # 2) Matrix Sum (2D List + Nested Loop)
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# result_sum = 0
# for row in matrix:
#     for col in row:
#         result_sum += col
# print(result_sum)
#
# row_sum_list = []
# for row in matrix:
#     row_sum = 0
#     for col in row:
#         row_sum += col
#     row_sum_list.append(row_sum)
# print(row_sum_list)
#
# col_sum_list = [0] * len(matrix[0])
#
# for row in matrix:
#     print(row)
#     for col_index in range(len(row)):
#         col_sum_list[col_index] += row[col_index]
#
# print(col_sum_list)


## # 3) Translator
# def translate(sentence):
#     translated_sentence = ""
#     for i in sentence:
#         if i.lower() in "aeiou":
#             translated_sentence = translated_sentence + "*"
#         else:
#             translated_sentence += i
#     return translated_sentence
# print(translate("Apple 123"))

# # 4) Safe division with try/except

# def safe_divide(a, b):
#     try:
#         return(a/b)
#     except ZeroDivisionError as err:
#         return err
#     except TypeError as err:
#         return str(err)
#
# print(safe_divide(4,"a"))

# # # 5) File handling
# numbers_file = open("numbers.txt","r")
# count_of_numbers = 0
# sum_of_numbers = 0
# count_negative_numbers = 0
#
# for num in numbers_file.readlines():
#     try:
#         count_of_numbers += 1
#         sum_of_numbers += int(num)
#         if int(num) < 0:
#             count_negative_numbers += 1
#     except ValueError:
#         continue
#
#
# print(count_of_numbers)
# print(sum_of_numbers)
# print(count_negative_numbers)
#
# numbers_file.close()