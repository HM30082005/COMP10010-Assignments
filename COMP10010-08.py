# # message = input('Enter ur message: ')
# # new_message = ""
# # VOWELS = "aeiou"

# # print()
# # for letter in message:
# #     if letter.lower() not in VOWELS:
# #         new_message += letter
# #         print(f"A new message has been created: {new_message}")

# # VOWELS = message

# # new_message = ""
# # print('Lets try again')
# # for letter in message:
# #     if letter.lower() not in VOWELS:
# #         new_message += letter
# #         print(f"A new message has been created: {new_message}")
# # print('ur new message is', new_message)

# # print('Enter the beginning and ending index for your slice of "pizza".')
# # print("Press the enter key at 'Start' to exit.")

# # word = "pizza"

# # start = None
# # while start != "":
# #     start = (input("\nStart: "))

# #     if start:
# #         start = int(start)
        
# #         finish = int(input("Finish: "))

# #         print(f"word[{start}:{finish}] is {word[start:finish]}" )
    
# # input("\n\nPress any key to exit.")

# # ----------------------––––––––––––––––––––––––––––––––––––––––––––––––––––––
# # TUPLES

# inventory = ("sword", "armor", "shield", "healing potion")

# print("Your items: ")
# for item in inventory:
#     print(item)

# print(f"You have {len(inventory)} items in your possesion")

# if "healing potion" in inventory:
#     print("You will ive to fight another day")

# # slicing

# start = int(input("\n Enter the index number to begin with: "))
# finish = int(input("\n Enter the index number to end with: "))

# print(inventory[start:finish])

# chest = ("gold", "gems")
# print(f"You find a chest. It contains {chest}. You add finding to your iventory. Your invetory is now {inventory + chest}")

for i in range(2, 5):
    print(i)