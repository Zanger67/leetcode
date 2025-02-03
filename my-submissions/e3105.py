class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        output, up_down, cnt = 0, None, 1
        for i, j in zip(nums[:-1], nums[1:]) :
            # Equal is not strict so reset
            if i == j :
                output, cnt, up_down = max(output, cnt), 1, None
                continue

            # Previous DNE / is equal case
            if up_down is None :
                cnt, up_down = 2, (i < j)
                continue

            # Previously going up
            if up_down :
                if i < j :
                    cnt += 1
                    continue
                output, cnt, up_down = max(output, cnt), 2, not up_down
                continue

            # Previously going down
            if i > j :
                cnt += 1
                continue
            output, cnt, up_down = max(output, cnt), 2, not up_down

        return max(output, cnt)
