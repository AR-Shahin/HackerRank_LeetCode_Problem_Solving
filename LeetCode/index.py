 
class Solution:
    def numWaterBottles(self, numBottles,numExchange):
        
        totalBottle = numBottles
        
        while numBottles >= numExchange:
            exchange = numBottles // numExchange
            
            emptyHave = numBottles - (exchange * numExchange)
            
            totalBottle += exchange
            
            numBottles = emptyHave + exchange
        
        return totalBottle
    
s = Solution();

numBottles = 15
numExchange = 4

print(s.numWaterBottles(numBottles,numExchange))

