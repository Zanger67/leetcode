class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        output = 0
        pref_sum = 0
        evens, odds = 1, 0
        for num in arr :
            pref_sum += num
            if pref_sum % 2 : # odd
                output += evens
                odds += 1
            else :
                output += odds
                evens += 1
        return output % (10 ** 9 + 7)
