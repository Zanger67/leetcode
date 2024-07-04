class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        counter = 0
        for k in range(len(arr) - 1, 0, -1) :
            current = arr[k]
            for i in range(k - 1, -1, -1) :
                current ^= arr[i]
                if (current == 0) :
                    # counter += 1
                    counter += k - i
        return counter