class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        return max(
            [-1] + 
            [
                sum(heapq.nlargest(2, [-inf] + list(group[1]))) 
                for group in groupby(
                    sorted(nums, key=lambda y: sum(map(int, str(y)))),
                    key=lambda x: sum(map(int, str(x)))
                )
            ]
        )