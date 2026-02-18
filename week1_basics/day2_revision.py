# # Mad Libs game
#
color = input("Enter a color: ")
plural_tone = input("Enter a plural :")
celeb = input("Enter a celebrity: ")


print(f"Roses are {color}")
print(f"{plural_tone} are blue")
print(f"I like {celeb}")
#
#

#  # List
friends = ["Brian", "Jacob", "Adam","Alan","Joe"]

print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[1] = "Joseph"
print(friends)
friends.insert(2,"Alice")
print(friends)

friends.remove("Joe")
print(friends)

list_of_num = [1, 2, 4, 6, 10, 8]
friends_t = ["Raj","Krish","Ram"]
friends_t.extend(list_of_num)
print(friends_t)
friends_t.append("Rahim")
print(friends_t)
friends_t.clear()
print(friends_t)
friends_t = ["Raj","Krish","Ram"]
friends_t.pop()
print(friends_t)

friends_t = ["Raj","Krish","Ram"]

print(friends_t.index("Ram"))

print(friends_t.count("Ram"))
friends_t.sort()
print(friends_t)
friends_t.reverse()
print(friends_t)

friends_2 = friends_t.copy()
print(friends_2)

