class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = 0
        numsFlipped = [False] * len(nums)
        flippedInWindow = 0

        hmap = (1, 0)

        for i, num in enumerate(nums) :
            if i >= k and numsFlipped[i - k] :
                flippedInWindow -= 1

            # odd number of flips
            if flippedInWindow % 2 :
                num = hmap[num]

            # is zero
            if not num :
                if i + k > len(nums) :
                    print(flips)
                    return -1
                
                flippedInWindow += 1
                flips += 1
                numsFlipped[i] = True

        return flips