#!/usr/bin/env python3
import random
import re
import os





def PassWord():

    punk = ["!",".","?","*","&"]
    Z = len(punk)
    space = " "


    input_string = input("\nEnter a minimum of five easily memorible words separated by space: ")
#    list  = input_string.split()
#    X = len(list)

#    list2  = input_string.split()
#    X2 = len(list2)


    #if X > 4:
        #main()

    input_int = input("\n Enter a minimum of 3 easy to remember number seperated by spaces(NO BIRTHDAYS: ")
    print("\n\n")
#        Num = input_int.split()
#        Y = len(Num)

    A = 2
    while A == 2:
        list  = input_string.split()
        X = len(list)
        list2  = input_string.split()
        X2 = len(list2)
        Num = input_int.split()
        Y = len(Num)

        list = random.choice(list)
        list = list
        list2 = random.choice(list2)
        Num = random.choice(Num)
        punk = random.choice(punk)
        BuildPass = []
        BuildPass.append(list.lower())
        BuildPass.append(space)
        BuildPass.append(list2.lower())
        BuildPass.append(Num)
        BuildPass.append(punk)
        random.shuffle(BuildPass)

        PassPass = BuildPass[0] + BuildPass[1] + BuildPass[2] + BuildPass[3] + BuildPass[4]
        PasswordA = PassPass.replace("a", "A")
        PasswordE = PasswordA.replace("e", "E")
        PasswordI = PasswordE.replace("i", "I")
        PasswordO = PasswordI.replace("o", "O")
        PasswordU = PasswordO.replace("u", "U")
        print("")
        print("Your password is:    " + PasswordU)
        print(" ")
        print("Would you like a diffrent password")
        B = input("NOTE: Selecting no will wipe screen(y,n)?  ")
        if B.lower() == "y":
            A = 2
        if B.lower() == "n":
            os.system('clear')
            A = 1

        
PassWord()