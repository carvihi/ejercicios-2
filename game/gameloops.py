#!/usr/bin/env python
# -*- coding: utf-8 -*-

secret = 5
guess = 0
congratulations = "Congratulations!"

greeting = "Welcome Smartninja. Today we will play to Guess the secret number. You must discover what is the secret number ... play?"
print greeting

while guess != secret:
    guess = int (raw_input("Enter your number (between 1 and 10): "))

    if guess == secret:
        print congratulations
        break
    elif guess > secret:
        print("Sorry try again...probably with a smaller number")
    elif guess < secret:
        print("Sorry try again...probably with a bigger number")



