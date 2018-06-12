"""greeting = "Welcome Smartninja. Today we will play to Guess the secret number. You must discover what is the secret number ... play?"
print greeting

secret = 5

congratulations = "Congratulations!"

guess = int (raw_input("Enter your number (between 1 and 10): "))
print guess

if guess == secret:
    print congratulations
else:
    print "Sorry, try again"
    """

#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Welcome Smartninja. Today we will play to Guess the secret number. You must discover what is the secret number ... play?"

import random

def main():

    secret = random.randint(1, 10)

    while True:
        guess = int(raw_input("Enter your number (between 1 and 10): "))
        if guess == secret:
            print "Congratulations!!! The secret number is " + str(secret)
            answer = raw_input("Would you like to start again? (yes/no):")
            if answer.lower() == "yes":
                main()
            if answer.lower() == "no":
                print "Thank you playing with us!!"
            break

        elif guess < secret:
            print "Sorry, try again with a bigger number"

        elif guess > secret:
            print "Sorry, try again with a smaller number"


if __name__ == "__main__":
    main()






