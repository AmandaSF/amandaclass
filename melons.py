"""This file should have our melon-type classes in it."""

class MelonOrder():
    species = None
    color = None
    imported = None
    shape = None
    seasons = None
    base_cost = 5.0
    import_fee = 1.5
    square_fee = 2.0

class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty >= 3:
            print "Watermelon price: " + str(qty * self.base_cost * 0.75)
        else:
            print "Watermelon price: " + str(self.base_cost * qty)   

melon = WatermelonOrder()
melon.get_price(4)

class CantaloupeOrder(MelonOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        if qty >= 5:
            print "Cantaloupe price: " + str(self.base_cost * qty * 0.5)
        else:
            print "Cantaloupe price: " + str(self.base_cost * qty)

melon = CantaloupeOrder()
melon.get_price(7)

class CasabaOrder(MelonOrder):
    species = "Casaba"
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        print "Casaba price: " + str(qty * (self.base_cost + 1) * self.import_fee)
        
melon = CasabaOrder()
melon.get_price(100)

class SharlynOrder(MelonOrder):
    species = "Sharlyn"
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        print "Sharlyn price: " + str(qty * self.base_cost * self.import_fee)

melon = SharlynOrder()
melon.get_price(50)

class SantaClausOrder(MelonOrder):
    species = "Santa Claus"
    color = "green"
    imported = True 
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        if self.imported == True:
            print "Santa Claus price: " + str(self.base_cost * qty * self.import_fee)

melon = SantaClausOrder()
melon.get_price(86648)

class ChristmasOrder(MelonOrder):
    species = 'Christmas'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        print "Christmas price: " + str(self.base_cost * qty)


melon = ChristmasOrder()
melon.get_price(6)

class HornedMelonOrder(MelonOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        print "Horned Melon price: " + str(qty * self.base_cost * self.import_fee)

melon = HornedMelonOrder()
melon.get_price(2)

class KiguaOrder(MelonOrder):
    species = 'Kigua'
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        print "Kigua Price: " + str(qty * self.base_cost * self.square_fee * self.import_fee)

melon = KiguaOrder()
melon.get_price(2)

class OgenOrder(MelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        print "Ogen price: " + str(qty * self.base_cost)

melon = OgenOrder()
melon.get_price(34)