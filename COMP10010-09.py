# week 8 lecture 1

# def fibonacciNumbers(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonacciNumbers(n - 1) + fibonacciNumbers(n - 2)
    
# num = int(input('n: '))
# print(fibonacciNumbers(num))

# import random as rand

# n = int(input('How many random numbers? '))

# # randlist = []
# randlist = ()
# for i in range(0, n):
#     temp = rand.randrange(0, 100),
#     randlist += temp
#     # randlist.append(temp)

# print('here is ur random sequence')
# print(randlist)

# sort_randlist = ()
# for i in range(0, n):
#     maxv = 0
#     maxp = -1
#     for j in range(0, len(randlist)):
#         if randlist[j] > maxv:
#             maxv = randlist[j]
#             maxp = j
#     sort_randlist += randlist[maxp],
#     randlist = randlist[0:maxp] + randlist[maxp+1:] # we cut out from the randlist tuble and then concatinate two cutouts

# print('and here it is sorted')
# print(sort_randlist)

#Hero's inventory 3.0

inventory = ['sword', 'armor', 'shield', 'healing potion']
print("Your items: ")
for item in inventory:
    print(item)

print(f"You have {len(inventory)} items in your posession")

if "healing potion" in inventory:
    print("You will live to fight another day")

index = int(input("\nEnter the index number of an item u wanna get: "))

print(f"At {index} is {inventory[index]}")
start = int(input("\n Enter the index number to begin with: "))
finish = int(input("\n Enter the index number to end with: "))

print(inventory[start:finish])
input('Any key to continuee.....\n')
chest = ["gold", "gems"]
print(f"You find a chest. It contains {chest}. You add finding to your iventory. Your invetory is now {inventory + chest}")

print('U give up ur sword for a crossbow')
inventory[0] = 'crossbow'
print(f"Your inventory is now {inventory}")

print('U buy orb of future telling with gems and gold')
inventory[4:6] = ["orb of future telling"]
print(f"Your inventory is now {inventory}")

print('Sheild was broken')
del inventory[2]
print(f"Your inventory is now {inventory}")

print('Ur crossbow and armor were stolen by thieves')
del inventory[:2]
print(f"Your inventory is now {inventory}")