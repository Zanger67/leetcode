# Squarely in the range of [30%, 60%]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        dequeeuueueueue = deque()
        dequeeuueueueue.extend([nums[(x - k + n) % n] for x in range(0, k)])
        for i in range(n) :
            dequeeuueueueue.append(nums[i])
            nums[i] = dequeeuueueueue.popleft()
