greeting = "Welcome Smartninja. Today we will play to Guess the secret number. You must discover what is the secret number ... play?"

print greeting

secret = 5

congratulations = "Congratulations!"

guess = int (raw_input("Enter your number: "))
print guess

if guess == secret:
    print congratulations
else:
    print "Sorry, try again"





