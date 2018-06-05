print "Welcome to FizzBuzz...Start the game!! (Please enter a whole number)"

while True:
    guess = int(raw_input("Select a number between 1 and 100: "))
    print guess

    for number in range(1,guess+1):
        if number % 3 == 0 and number % 5 == 0:
            print "fizzbuzz"
        elif number % 5 == 0:
            print "buzz"
        elif number % 3 == 0:
            print "fizz"
        else:
            print number


    answer = raw_input("Do you want to continue? yes/no: ")
    if answer.lower() == "yes":
        continue
    if answer.lower() == "no":
        break

print "Thank you for using our services. See you soon!!"




