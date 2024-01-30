# 11th October 2023

# c = 1
# while c<10:
#     print(c)
#     if c==5:
#         break
#     c += 1

# print("Exclusive compter network\n")
# print("Members only\n")

# security = 0

# username = ""
# while not username:
#     username = input("Username: ")

# password = ""
# while not password:
#     password = input("Password: ")

# if username == "M.Dawson" and password == "secret":
#     print("Hi, Mike.")
#     security = 5
# elif username == "S.Meier" and password == "civilization":
#     print("Hey, Sid.")
#     security = 3
# elif username == "S.Miyamoto" and password == "mariobros":
#     print("What's up, Shigeru?")
#     security = 3
# elif username == "W.Wright" and password == "thesims":
#     print("How goes it, Will?")
#     security = 3
# elif username == "guest" or password == "guest":
#     print("Welcome, guest.")
#     security = 1
# else:
#     print("Login failed. You're not so exclusive.\n")
# input("\n\nPress the enter key to exit.")

import random as rd

# name = input("What is your name?\n")

# try:
#     limit = int(input("Enter the highest possible number you want to be in a guessing list\n"))
# except:
#     print("Wrong input!")
#     exit()

# secret_number = rd.randint(1, limit)

# guess = 0
# count = 0

# while guess != secret_number:
#     guess = int(input("Your guess(numbers only):  "))
#     count += 1
#     if guess > secret_number:
#         print("Your guess is higher than the secret number")
#     if guess < secret_number:
#         print("Your guess is lower than the secret number")
#     if guess == secret_number:
#         print(f"You won in {count} guesses!\n")
#         break
#     else:
#         ans = input("Wanna play again?\n1 yes\n2 no\n")
#         if ans == "2" or ans == "no":
#             print("U lost...")
#             break
    

# Coin flip

# print("How many times do u want me to flip the coin?")

# while True:
#     try:
#         n = int(input("Enter the number: "))
#         break
#     except:
#         print("Wrong input, try again")

# count = 0
# tails = 0
# heads = 0
# while count != n:
#     test = rd.randint(1, 2)
#     count += 1
#     if test == 1:
#         tails += 1
#     elif test == 2:
#         heads += 1

# probt, probh = tails / count, heads / count
# print(f"Tails happened to fall {tails} times which is {probt * 100}% of all flips, heads happened to fall {heads} times which is {probh * 100}% of all flips,")

# word = input("Tell me a waord:\n")

# print("Here's each letter...")
# for letter in word:
#     print(letter)

# for i in range(-10, -100, -1):
#     print(i, end=" ")

#  Sum of cubes

n = int(input('Num: '))
sum = 0
for i in range(n + 1):
    sum += i * i * i
print(f"Sum of cubes of all natural numbers up to {n} is {sum}")