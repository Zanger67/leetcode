class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pref = [0] + list(accumulate(nums))
        two_sum = defaultdict(set)           # {difference val to k: [list of index sources]}

        for i, x in enumerate(pref) :
            two_sum[k + x].add(i)

        output = 0
        for i, x in enumerate(pref) :
            if x not in two_sum :
                continue
            for j in two_sum[x] :
                if j >= i :
                    continue
                output = max(output, abs(i - j))

        return output