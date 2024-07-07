class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        output = 0
        while numBottles >= numExchange :
            output += numBottles - numBottles % numExchange
            numBottles = numBottles % numExchange + numBottles // numExchange
        output += numBottles
        return output