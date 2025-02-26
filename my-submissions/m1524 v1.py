class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        for i in range(1, len(arr)) :
            arr[i] += arr[i - 1]

        output = 0
        evens, odds = 1, 0
        for i in range(len(arr)) :
            if arr[i] % 2 : # odd
                output += evens
                odds += 1
            else :
                output += odds
                evens += 1
        return output % (10 ** 9 + 7)
