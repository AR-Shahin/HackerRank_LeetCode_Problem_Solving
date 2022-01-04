

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        totalBottle = numBottles

        while numBottles >= numExchange:
            exchange = numBottles // numExchange

            emptyHave = numBottles - (exchange*numExchange)

            totalBottle += exchange

            numBottles = emptyHave + exchange
        return totalBottle


ob = Solution()
numBottles = 9
numExchange = 3
print(ob.numWaterBottles(numBottles, numExchange))
