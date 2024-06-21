class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        currentlySatisfied = sum(customers[x] for x in range(len(customers)) if not grumpy[x])
        satisfied = [0] * len(grumpy)

        maxx = 0

        for i in range(len(grumpy)) :
            if grumpy[i] :
                currentlySatisfied += customers[i]

            if i - minutes >= 0 and grumpy[i - minutes] :
                currentlySatisfied -= customers[i - minutes]

            if currentlySatisfied > maxx :
                maxx = currentlySatisfied

            satisfied[i] = currentlySatisfied

        return maxx