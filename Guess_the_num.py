import random

# function guess_step_bin(low, high):
#     guess = (low + high) // 2

def check(num, tar):
    if num < tar:
        print("\n\n*Mechanical voice* TOO LOW\n\n")
        input("Press any key to continue\n")
        return 0
    if num > tar:
        print("\n\n*Mechanical voice* TOO HIGH\n\n")
        input("Press any key to continue\n")
        return 1

name = input('Hi, I am the curent champion of guess the number. U wanted to challange me *clearing throat* get trashed. But wanyway I am always ready to take a challange! Whats ur name?\n')
rules = input(f"Okay, {name}, for starters to you know the rules?(Yes/No)\n")
if rules.lower() == "no":
    print(f"{name}, {name}... *sigh* You want to challange me an dont even know the rules... That's just sad at this point...")
    print("But, anyway, rules are quite simple,\n there's a random number from 1 to 128, then you we toss a coin and whoever wins starts first, then the first calls a number.\n If u didnt get it right u find out whether u have to go lower or higher, and if you guess it.. well u win, but dont worry about that not gonna happen. Understood?")
input('Ready to start, then?')
magic = random.randint(1, 128)
print('*Machine says* NUMBER HAS BEEN SELECTED')
coin_str = input("Now we toss a coin, pick heads or tails\n")
if coin_str.lower() == 'heads':
    coin = 1
elif coin_str.lower() == 'tails':
    coin = 2
else:
    print("Well if you cant even type properly u r not a proper challanger, bye bye, see u when u'll get to terms with ur keyboard")
    exit()

coin_toss = random.randint(1, 2)
if coin_toss == 1:
    print('Heads!')
else:
    print('Tails!')
turn_order = 0
if coin_toss == coin:
    print("U go first, not like it's gonna help you..")
    turn_order = 0
else:
    print("Ooops, seems Im going first. I suggest u to pray... u gotta rely on god to beat me in this condiotions")
    turn_order = 1
player_guess = 0
guess = 0
low, high = 1, 128
while (True):
    if turn_order == 0:
        player_guess = int(input("*mechanical voice* TELL ME A NUMBER\n\n"))
        check(player_guess, magic)
        if player_guess == magic:
            print("Noooooo! How did you beat me!!... *crying* I will never forgive you see u another time.. The time when Im gonna trash you.")
            exit()
        guess = (low + high) // 2
        print(f"*mechanical voice* TELL ME A NUMBER \n \t I'll go with {guess}")
        guide = check(guess, magic)
        if guess == magic:
            print("Too eaaasssyyyyy! U need to practice more!")
            exit()
        if guide == 0: 
            low = guess
        elif guide == 1:
            high = guess
    else:
        guess = (low + high) // 2
        print(f"*mechanical voice* TELL ME A NUMBER \n \t I'll go with {guess}")
        guide = check(guess, magic)
        if guess == magic:
            print("Too eaaasssyyyyy! U need to practice more!")
            exit()
        if guide == 0: 
            low = guess
        elif guide == 1:
            high = guess
        player_guess = int(input("*mechanical voice* TELL ME A NUMBER\n\n"))
        check(player_guess, magic)
        if player_guess == magic:
            print("Noooooo! How did you beat me!!... *crying* I will never forgive you see u another time.. The time when Im gonna trash you.")
            exit()


