#There will be two players and 5 stocks
#the play mode will be:
#Players starts with 1000 cash
#Stocks start at a random number between 1 and 1000
#Players purchase stocks
#After selling purchases players end turn
#at the end of both turns, stocks randomly change
#This ends the day and the players make their purchases sales and stocks change until days run out and winning player is decided by how much money/value they have

import random
    

#create class Player
#Player has Position, Cash, and Stocks
#Player initiates with Cash
class Player(object):

    def __init__(self, cash):
        self.cash = cash
        
    def bid_position(self, bid):
        self.bid = bid

#create class Stock
#Stock has Risk, Quantity, and Value
#Stock initiates with random Risk, Quantity, and Value
class Stock(object):
    

    def __init__(self):
        self.risk = random.random()
        self.quantity = random.randint(0,1000)
        self.value = random.randint(0,100)
 
class Game(object):
    def __init__(self):
        playerA = Player(1000)
        playerB = Player(1000)
        stockA = Stock()
        print "stockA risk: " + str(stockA.risk)
        print "stockA quantity: " + str(stockA.quantity)
        print "stockA value: " + str(stockA.value)
        stockB = Stock()
        print "stockB risk: " + str(stockB.risk)
        print "stockB quantity: " + str(stockB.quantity)
        print "stockB value: " + str(stockB.value)
        stockC = Stock()
        print "stockC risk: " + str(stockC.risk)
        print "stockC quantity: " + str(stockC.quantity)
        print "stockC value: " + str(stockC.value)
        stockD = Stock()
        print "stockD risk: " + str(stockD.risk)
        print "stockD quantity: " + str(stockD.quantity)
        print "stockD value: " + str(stockD.value)
        stockE = Stock()
        print "stockE risk: " + str(stockE.risk)
        print "stockE quantity: " + str(stockE.quantity)
        print "stockE value: " + str(stockE.value)

        
if __name__ == "__main__":
    gameOne = Game()