class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        maxWarehouse = [warehouse[0]] + [0] * (len(warehouse) - 2) + [warehouse[-1]]

        for i in range(1, len(warehouse)) :
            maxWarehouse[i] = min(maxWarehouse[i - 1], warehouse[i])

        maxWarehouse[-1] = max(maxWarehouse[-1], warehouse[-1])
        for i in range(len(warehouse) - 2, -1, -1) :
            maxWarehouse[i] = min(warehouse[i], max(maxWarehouse[i + 1], maxWarehouse[i]))

        maxWarehouse.sort()
        boxes.sort()

        counter = 0
        while maxWarehouse and boxes :
            if boxes[-1] <= maxWarehouse[-1] :
                counter += 1
                maxWarehouse.pop()
            boxes.pop()

        return counter