factor = 0.62137

print "Hello SmartNinja. This program help you to convert kilometers to miles"
while True:
    km = raw_input("Insert your kilometer value: ")
    print km

    miles = round(float(km) * factor, 2)
    print miles

    answer = raw_input("Do you want to continue? yes/no: ")
    if answer.lower() == "yes":
        continue
    if answer.lower() == "no":
        break
    print "Sorry, invalid answer. Start again"

print "Thank you for using our services. See you soon!!"



