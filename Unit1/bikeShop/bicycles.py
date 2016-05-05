import random

class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
    def __repr__(self):
        return self.model

class BikeShop(object):
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.margin = margin
    
    def profit(self, bike):
        return self.margin * bike.cost
       
    def afford(self, cust):
        affordableBikes = []
        for bike in self.inventory:
            #print(bike)
            if bike.cost <= cust.wallet:
                affordableBikes.append(bike.model)
        return affordableBikes
    
    def buy(self, cust):
        affordableBikes = []
        for bike in self.inventory:
            if bike.cost <= cust.wallet:
                affordableBikes.append(bike)
        
        bikePurchase = random.choice(affordableBikes)
        cust.wallet = cust.wallet - bikePurchase.cost

        for bike in self.inventory:
            if bikePurchase.model == bike.model:
                self.inventory[bike] = self.inventory[bike] - 1
                #print("Number of {} now in stock: {}".format(bike.model, self.inventory[bike]))
        return bikePurchase
        
class Customer(object):
    def __init__(self, name, wallet, ownBike):
        self.name = name
        self.wallet = wallet
        self.ownBike = ownBike