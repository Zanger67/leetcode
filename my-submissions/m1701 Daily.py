class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        output = 0
        currentTime = customers[0][0]
        custCount = len(customers)

        for i, customer in enumerate(customers) :
            if customer[0] > currentTime :
                currentTime = customer[0]
            output += (currentTime + customer[1]) - customer[0]
            currentTime += customer[1]
            
        return output / custCount