class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = deque(sorted(nums))
        output = []

        while nums :
            output.append((nums.popleft() + nums.pop()) / 2)

        return min(output)