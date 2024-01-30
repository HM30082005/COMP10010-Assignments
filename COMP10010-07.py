# message analyzer
# message = input('Enter your message: ')
# print(f"The legth og you message is {len(message)}")

# print('The most populat letter of the english language "e", ', end="")

# if 'e' in message:
#     print('is in your message')
# else:
#     print('is not in your message')

# import random

# word = "index"

# print(f"The word is {word} \n")
# high = len(word)
# low  = -len(word)

# for i in range(10):
#     position = random.randrange(low, high)
#     print(f"word [{position}]\t{word[position]}")

# wrong index

# word = input("gimme a ward: ")
# endw = len(word)
# i = 0
# while i < endw:
#     print(f"{i} is {word[i]}")
#     i += 1

message = input('Enter ur message: ')
new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print(f"A new message has been created: {new_message}")