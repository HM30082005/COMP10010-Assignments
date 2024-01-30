# Second assignment// worth 12% 
name = input("What is your name?")

# height can be inputed as integer or float
height_cm = float(input("What is your height in centimeters?"))

# feet rounded down
feet = int(height_cm * 0.0328)
# total amount of inches
inch = 0.394 * height_cm
# removing inches that are already counted within feet
inch -= feet * 12
# rounding down inches and getting the excess
inch, qinch = divmod(inch, 1)
# translating excess to quater inches
qinch *= 4
# it was decided to give the closest number there is, soo 
# in case if it turns out that there are pretty much 4 quater inches, we'll just add another inch 
if 4 == round(qinch):
    qinch = 0
    inch += 1
# printing the result with cool formated string
# I promise not plagirism, I cna write it the other way too: 
# print("Dear", name.upper(), "you are", feet, "ft", int(inch), round(qinch), end = "")
# print("/4 in tall")
print(f"Dear {name.upper()} you are {feet} ft {int(inch)} {round(qinch)}/4 in tall")