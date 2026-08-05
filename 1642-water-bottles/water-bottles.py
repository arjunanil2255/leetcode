class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        total = 0
        while numBottles > 0:
            total += numBottles
            empty += numBottles

            numBottles = empty // numExchange
            empty = empty % numExchange 

        return total    