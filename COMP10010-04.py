import random

# freq = {}

# die1 = random.randint(1, 6)
# print(die1)
# for i in range(100):
#     die1 = random.randint(1, 6)
#     if str(die1) in freq:
#         freq[str(die1)] += 1
#     else:
#         freq[str(die1)] = 1

# print(freq)

# if-statement 
# print("Welcome to the System Security Inc.")

# password = input("Enter your password: ")
# if password == "secret":
#     print("Access Granted")
# else:
#     print("Access denied")

# input('Press any key to continue...')

# 3

print ("""
1 New game
2 Load game
3 Save game
4 Exit
""")
try:
    choice = int(input("Your choice: "))
    if choice == 1:
        print("New Game, not implemented yet...")
    elif choice == 2:
        print("Load Game, not implemented yet...")
    elif choice == 3:
        print("Save, not implemented yet...")
    elif choice == 4:
        print("Exiting")
    else:
        print("Unknown input")
except:
    print("Unknown input")
