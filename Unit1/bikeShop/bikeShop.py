import random

class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
    def __repr__(self):
        return "OBJECT" + self.model

class BikeShop(object):
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.margin = margin
    
    def profit(self, bike):
        return "%.2f" % (self.margin * bike.cost)
       
    def afford(self, cust):
        affordableBikes = []
        for bike in self.inventory:
            #print(bike)
            if bike.cost < cust.wallet:
                affordableBikes.append(bike.model)
        return affordableBikes
    
    def buy(self, cust):
        affordableBikes = []
        for bike in self.inventory:
            #print(bike)
            if bike.cost < cust.wallet:
                affordableBikes.append(bike)
        bikePurchase = random.choice(affordableBikes)
        cust.wallet = cust.wallet - bikePurchase.cost
        return bikePurchase.model


class Customer(object):
    def __init__(self, name, wallet, ownBike):
        self.name = name
        self.wallet = wallet
        self.ownBike = ownBike
        
huffy = Bicycle("Huffy", 50, 175)
mongoose = Bicycle("Mongoose", 40, 199)
diamondback = Bicycle("Diamondback", 48, 155)
schwinn = Bicycle("Schwinn", 38, 349)
trek = Bicycle("Trek", 36, 1199)
giant = Bicycle("Giant", 52, 215)
fuji = Bicycle("Fuji", 35, 489)
redline = Bicycle("Redline", 30, 699)

bob = Customer("Bob", 200, False)
sally = Customer("Sally", 500, False)
joe = Customer("Joe", 1000, False) 

acmeShop = BikeShop("Acme Bike Shop", [huffy, mongoose, diamondback, schwinn,
                                        trek, giant, fuji, redline], 0.2)

print("Hello and welcome to {}!  We currently have the following bikes in stock:\n".format(acmeShop.name))
for bike in acmeShop.inventory:
    print(bike.model, end=", ")
print("")
print("")

input("Press enter to continue.")

print("{}, you have ${} to spend.  With that budget you can buy the following bikes:\n".format(bob.name, str(bob.wallet)))
print(", ".join(acmeShop.afford(bob)))
print("")
print("Which bike would you like to purchase?")
input("Press enter to continue")
print("Bob chose the " + str(acmeShop.buy(bob)) + ".  Great choice!  Bob has ${} left in his budget.".format(str(bob.wallet)))


''' 
KEEP THESE FOR LATER:





print(acmeShop.profit(huffy))
print(acmeShop.profit(mongoose))
print(acmeShop.profit(diamondback))
print(acmeShop.profit(schwinn))
print(acmeShop.profit(trek))
print(acmeShop.profit(giant))
print(acmeShop.profit(fuji))
print(acmeShop.profit(redline))
'''