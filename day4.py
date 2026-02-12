# # Dictionaries

week_days = {
    "Mon" : "Monday",
    "Tues" : "Tuesday",
    "Wed" : "Wednesday",
    "Thurs" : "Thursday",
    "Fri" : "Friday",
    "Sat" : "Saturday",
    7 : "Sunday",
}

print(week_days)

print(week_days["Mon"])
print(week_days["Tues"])
print(week_days.get("Wed"))
print(week_days.get("POS"))
print(week_days.get("POS","Invalid Key"))
print(week_days[7])
# print(week_days["POS"])


# # While Loop
i = 1
while i <= 5:
    print(i)
    i += 1
print("THE END")


# # Guess Game:
# User has to guess a word
# has 3 limits
# if guess limit exceeds, print you lose
# if guess is correct, print you win

secret_word = "secret"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while secret_word != guess_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess_word = input("Enter a guess word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You Lose!")

else:
    print("You Win!")


# # For Loop:
for letter in "ABCD EFGH":
    print(letter)

friends = ["Ram", "Robert", "Rahim"]

for friend in friends:
    print(friend)

for i in range(5):
    print(i)

for i in range(3,5):
    print(i)

for i in range(4):
    if i == 0:
        print("first")
    else:
        print("not first")