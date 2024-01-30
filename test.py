height = 0
while height < 1000000:
    feet = int(height/30.48)
    inch = int(((height/30.48) -int(height/30.48))*12)
    quarter= round((((height/30.48)-int(height/30.48))*12 - int(((height/30.48)-int(height/30.48))*12))*4)
    # name=name.upper()
    # print("dear",name,"you are",feet,"ft",inch,  quarter, end = "/4 in tall")
    if 4 == round(quarter):
        quarter = 0
        inch += 1


# feet rounded down
    feet1 = int(height * 0.0328)
# total amount of inches
    inch1 = 0.394 * height
# removing inches that are already counted within feet
    inch1 -= feet * 12
# rounding down inches and getting the excess
    inch1, qinch = divmod(inch1, 1)
# translating excess to quater inches
    qinch *= 4
# it was decided to give the closest number there is, soo 
# in case if it turns out that there are pretty much 4 quater inches, we'll just add another inch 
    if 4 == round(qinch):
        qinch = 0
        inch1 += 1
# printing the result with cool formated string
# I promise not plagirism, I cna write it the other way too: 
# print("Dear", name.upper(), "you are", feet, "ft", int(inch), round(qinch), end = "")
# print("/4 in tall")
    # print(f"Dear {name.upper()} you are {feet1} ft {int(inch1)} {round(qinch)}/4 in tall")

    if round(qinch) != quarter or int(inch1) != inch or feet != feet1:
        print(f"Mistake , hight {height}")
        print(feet, inch, quarter)
        print(feet1, int(inch1), round(qinch))
        break 
    height += 1

