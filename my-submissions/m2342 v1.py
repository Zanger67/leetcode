class Solution:
    def digit_sum(self, num: int) -> int :
        output = 0
        while num :
            output += num % 10
            num //= 10
        return output

    def maximumSum(self, nums: List[int]) -> int:
        digit_sums = [self.digit_sum(num) for num in nums]

        digit_sum_indxs = defaultdict(list)
        for i, x in enumerate(digit_sums) :
            digit_sum_indxs[x].append(i)

        output = -1
        for freq, indxs in digit_sum_indxs.items() :
            if len(indxs) < 2 :
                continue
            output = max(output, sum(sorted([nums[x] for x in indxs])[-2:]))
        return output