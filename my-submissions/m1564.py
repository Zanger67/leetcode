class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)) :
            warehouse[i] = min(warehouse[i], warehouse[i - 1])

        boxes.sort(reverse=True)

        counter = 0
        while boxes and warehouse :
            if boxes[-1] <= warehouse[-1] :
                counter += 1
                boxes.pop()
            warehouse.pop()
        return counter