class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

class BikeShop(object):
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.margin = margin
    
    def profit(self, bike):
        return "%.2f" % (self.margin * bike.cost)
'''        
    def afford(self, cust):
        affordableBikes = []
        for i in self.inventory:
            if self.inventory < cust.wallet:
                affordableBikes.append(bike.model)
        return affordableBikes
'''
class Customer(object):
    def __init__(self, name, wallet, ownBike):
        self.name = name
        self.wallet = wallet
        self.ownBike = ownBike
        
huffy = Bicycle("Huffy", 50, 199)
mongoose = Bicycle("Mongoose", 40, 249)
diamondback = Bicycle("Diamondback", 48, 249)
schwinn = Bicycle("Schwinn", 38, 349)
trek = Bicycle("Trek", 36, 1199)
giant = Bicycle("Giant", 52, 149)
fuji = Bicycle("Fuji", 35, 489)
redline = Bicycle("Redline", 30, 699)

bob = Customer("Bob", 200, False)
sally = Customer("Sally", 500, False)
joe = Customer("Joe", 1000, False) 

acmeShop = BikeShop("Acme Bike Shop", [huffy, mongoose, diamondback], 0.2)


#print("Hello PLACEHOLDER and welcome to PLACEHOLDER!  Based on your budget, you can afford the following bicycles:")
#print(acmeShop.afford(bob))


print(acmeShop.profit(huffy))
print(acmeShop.profit(mongoose))
print(acmeShop.profit(diamondback))
print(acmeShop.profit(schwinn))
print(acmeShop.profit(trek))
print(acmeShop.profit(giant))
print(acmeShop.profit(fuji))
print(acmeShop.profit(redline))
