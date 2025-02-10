class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        moves = 0
        curr_sum = 0

        # Min heap keeps the largest abs val neg numbers at top
        neg_hp = []

        for num in nums :
            if num < 0 :
                heapq.heappush(neg_hp, num)

            curr_sum += num
            if curr_sum < 0 :
                moves += 1
                curr_sum -= heapq.heappop(neg_hp)

        return moves