#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Welcome to the daily Restaurant menu program."

menu_dict = {}

while True:
    dish1 = raw_input("Please select a first dish: ")
    price1 = raw_input("Please enter the dish price:")
    print "Your first dish is: " + dish1 + price1

    menu_dict[dish1] = price1


    dish2 = raw_input("Please select a second dish: ")
    price2 = raw_input("Please enter the dish price:")
    print "Your first dish is: " + dish2 + price2

    menu_dict[dish2] = price2

    dish3 = raw_input("Please select a dessert: ")
    price3 = raw_input("Please enter the dessert price:")
    print "Your first dish is: " + dish3 + price3

    menu_dict[dish3] = price3

    final = raw_input("Have you completed your menu? (yes/no) ")


    if final.lower() == "no":
        continue

    if final.lower() == "yes":
        menu_file = open ("menu.txt", "w+")

        print "Your menu is:"
        menu_file.write("Your menu is:\n")
        for key, value in menu_dict.items():
            print "- " + key + "," + value
            menu_file.write("- "+ key + "," + value + "\n")


        menu_file.close()

        break

print "Thank you to use our service."
