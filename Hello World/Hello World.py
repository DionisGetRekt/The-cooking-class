import time
#Ask the user what his name is
name=input("What is your name?")

#prints "Hello" followed by the user's name
print("Hello "+name+"!")

#Ask the user how old he/she is
age=float(input("How old are you?"))

#If user's age is smaller or equal to 18 then the user cannot enter
if age <= 18:
    print("Sorry "+name+" but you cannot take this class if you are under 18 years old!")
else:
    print("Welcome to this class, "+name+"!")
    time.sleep(5)
    print("OK! Let's begin this lesson!")
    time.sleep(2)
    faving = input("First,I must know what is your favourite ingredient, " + name + ".")
    time.sleep(2)
    print("Perfect! "+faving+" is my favourite ingredient too!")
    time.sleep(1)
    favfood = input("Now I have to know what your favourite dish is!")
    time.sleep(3)
    print("WOW, we have a lot in common, "+name+"!")
    print("*fire alarm goes off*")
    time.sleep(3)
    print("OK, students, calm down, the fire alarm just went off! Please leave this classroom quietly!")

