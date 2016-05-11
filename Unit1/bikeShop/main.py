from bicycles import Bicycle
from bicycles import BikeShop
from bicycles import Customer

#Bicycles
huffy = Bicycle("Huffy", 50, 175)
mongoose = Bicycle("Mongoose", 40, 199)
diamondback = Bicycle("Diamondback", 48, 155)
schwinn = Bicycle("Schwinn", 38, 349)
trek = Bicycle("Trek", 36, 1199)
giant = Bicycle("Giant", 52, 215)
fuji = Bicycle("Fuji", 35, 489)
redline = Bicycle("Redline", 30, 699)

#Customers
bob = Customer("Bob", 200, False)
sally = Customer("Sally", 500, False)
joe = Customer("Joe", 1000, False) 

#Shop
acmeShop = BikeShop("Acme Bike Shop", {huffy:10, mongoose:20, diamondback:30, schwinn:40,
                                        trek:50, giant:60, fuji:70, redline:80}, 0.2)
                                    #list search: O(n) order-n
                                    #dictionary search: O(1) order 1 or constant
                                    #alternate: {'Huffy':(huffy, 10)}
                                    #inventory['huffy'][1] is the number of bikes in inventory

#Introduction
print("Hello and welcome to {}!  We currently have the following bikes in stock:\n".format(acmeShop.name))
for bike, quantity in acmeShop.inventory.items():
    print(bike.model, quantity, end=", ")
print("")
print("--------------------")
input("Press enter to continue.")
print("--------------------")

#Action
totalProfit = 0
for customer in [bob, sally, joe]:
    print("{}, you have ${} to spend.  With that budget you can buy the following bikes:\n".format(customer.name, str(customer.wallet)))
    print(", ".join(acmeShop.afford(customer)))
    print("")
    print("Which bike would you like to purchase?")
    print("--------------------")
    input("Press enter to continue")
    print("--------------------")
    customersBike = acmeShop.buy(customer)
    print("*** {} chose the ".format(customer.name) + str(customersBike) + ".  Great choice!  {} has ${} left. ***".format(customer.name, str(customer.wallet)))
    print("Number of {} now in stock: {}".format(customersBike.model, acmeShop.inventory[customersBike]))
    print("{}'s profit off of this sale:".format(acmeShop.name))
    print(acmeShop.profit(customersBike))
    totalProfit = totalProfit + acmeShop.profit(customersBike)
    print("--------------------")
    input("Press enter to continue")
    print("--------------------")
    print("Inventory after purchases:\n")
    for bike, quantity in acmeShop.inventory.items():
        print(bike.model, quantity, end=", ")
    print("\n")
    print("Total shop profit from today's purchases:\n")
    print(totalProfit)