class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCounter = 0
        output = 0
        
        sumTracker = defaultdict(int)
        sumTracker[0] = 1

        for num in nums :
            oddCounter += num % 2

            pairedValue = oddCounter - k
            if pairedValue in sumTracker :
                output += sumTracker[pairedValue]

            sumTracker[oddCounter] = sumTracker[oddCounter] + 1

        return output