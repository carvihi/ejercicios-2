#!/usr/bin/env python
# -*- coding: utf-8 -*-

class vehicle:
    def __init__(self, brand, model, kilometers, service):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.service = service

    def get_full_name(self):
        return self.brand + " " + self.model

def list_all(vehicles):
    for index, car in enumerate(vehicles):
        print "ID: " + str(index)
        print car.brand
        print car.model
        print car.kilometers
        print car.service
        print ""

    if not vehicles:
        print "You don't have any vehicle in your Vehicle database, please add a new vehicle."

def add(vehicles):
    brand = raw_input("Please enter the brand vehicle: ")
    model = raw_input("Please enter the model vehicle: ")
    kilometers = raw_input("Please enter the kilometers of vehicle: ")
    service = raw_input("Please enter the service date: ")

    new = vehicle(brand=brand, model=model, kilometers=kilometers, service=service)
    vehicles.append(new)

    print ""
    print "Vehicle added"

def edit(vehicles):
    for index, car in enumerate(vehicles):
        print "ID: " + str(index) + ") " + car.get_full_name()
    print ""

    id_question = raw_input("What vehicle would you like to edit? (enter ID number): ")
    selection = vehicles[int(id_question)]

    new_kilometers = raw_input("Please enter new kilometers for %s: " % selection.get_full_name())
    selection.kilometers = new_kilometers

    new_service = raw_input("Please enter the new service date for %s: " % selection.get_full_name())
    selection.service = new_service

    print ""
    print "Vehicle updated."


def main():

    print "Welcome to your Vehicle manager program"

    car1 = vehicle(brand="Citroen", model="Berlingo", kilometers="12564", service="06/09/2019")
    car2 = vehicle(brand="Renault", model="Traffic", kilometers="25631", service="10/11/2018")
    car3 = vehicle(brand="Citroen", model="Jumpy", kilometers="235987", service="17/05/2020")

    vehicles = [car1, car2, car3]

    while True:
        print ("-" * 100)
        print "Please choose one of these options:"
        print ("=" * 100)
        print "a) See all your vehicles"
        print "b) Add a new vehicle"
        print "c) Edit a vehicle"
        print "d) Quit the program."
        print ("-" * 100)

        selection = raw_input("Enter your selection (a, b, c, or d): ")
        print ""

        if selection.lower() == "a":
            list_all(vehicles)
        elif selection.lower() == "b":
            add(vehicles)
        elif selection.lower() == "c":
            edit(vehicles)
        elif selection.lower()  == "d":
            print ("=" * 100)
            print "Thank you to use our service"
            break


    vehicle_file = open("vehicle.txt", "w+")

    vehicle_file.write("Your list of vehicles is:\n")
    for index, car in enumerate(vehicles):
        vehicle_file.write("ID: " + str(index) + ") " + car.get_full_name() + "\n")

    vehicle_file.close()


if __name__ == "__main__":

    main()



"""menu = [list_all(vehicles), add(vehicles), edit(vehicles)]
    for items in menu:
        if 
        else selection.lower() == "d":
            print ("=" * 100)
            print "Thank you to use our service"
            break"""