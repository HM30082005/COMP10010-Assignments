# This function checks if charachter is Alphanumerical, i.e. it is a number or a letter.
def alphaNumerical(c):
    # I compare ASCII code of charachter from the string with ACSII codes of letters, capital letters and numbers to find out if it is one of them.
    # This works since in ASCII table all small letters, all capital letters and all numbers from 0 to 9 go in a row
    if (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')):
        return True
    else:
        return False

def isPalindrome(word):
    # I create two pointers the left one and the right one and set them to the ends of the string
    l = 0
    r = len(word) - 1
    while l < r:
        # now I increase the left pointer until I encounter an alphanumerical charachter
        while l < r and not alphaNumerical(word[l]):
            l += 1
        # now I decrease the right pointer until I encounter an alphanumerical charachter
        while l < r and not alphaNumerical(word[r]):
            r -= 1
        # Once I encountered Alphanumerical charachter on the right and on the left I comper them, ignoring the case(using the finction lower)
        if word[l].lower() != word[r].lower():
            return False # if they are not equal, the funtion returns false as word is not a palindrome
        l += 1 # move l by 1 to the right
        r -= 1 # move r by 1 to the left
    return True # if none of the elements were not equal, the word is a palindrome and we return it 

while True: #infinite loop
    word = input("Enter the word that you want to test (spces and other not alphanumerical charachters will be ignored): ") #asking user for a word
    while word == '':#if they dont give a anything and just press enter
        print('Im afraid you will have to input something')
        word = input("Enter the word that you want to test (spces and other not alphanumerical charachters will be ignored): ")#we keep asking them
    if isPalindrome(word):#using the function to find out if string is a palidrome
        print(f"'{word}' is a palindrome")#tell user the answer
    else:
        print(f"'{word}' is not a palindrome")#tell user the answer
    choice = input("Type Y if you want to continue and any other letter if not ")#ask them if they want to continue
    if choice.lower() != "y": #if not break the infinite loop and the program will finish
        print('Goodbye.')
        break

