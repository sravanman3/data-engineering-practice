# Mad Libs Game
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print(f"Roses are {color}")
print(f"{plural_noun} are blue")
print(f"I like {celebrity}")

# #Lists
friends = ["Vijay", "Ram", "Prabhas","Anand","Mahesh"]
print(friends) # print list
print(friends[1]) # print value at index 1 - indexes start with 0 in Python
print(friends[-1]) #Access elements in reverse - index start with -1

print(friends[1:]) #Access range of elements from list starting at index position 1 till end
print(friends[1:4]) #Range from index 1 till 4-1 = 3

friends[3] = "Ravi"
print(friends[3])


# # List Functions
lucky_numbers = [10,3,4,23]
friends = ["John", "Adam", "Jacob", "Rick", "Steve"]
print(friends)
# friends.extend(lucky_numbers)
# print(friends)

friends.append("Rogers")
print(friends)

friends.insert(1,"Stone")
print(friends)

friends.remove("Stone")
print(friends)

friends.sort()
print(friends)

friends.pop()
print(friends)

print(friends.index("Adam"))
print(friends.count("Adam"))
friends.sort()
print(friends)

friends.reverse()
print(friends)

friends1 = friends.copy()
print(friends1)
friends1.insert(1,"Jennifer")
print(friends1)
print(friends)

friends2 = friends1
print(friends2)
friends2.remove("Jennifer")
print(friends2)
print(friends1)
