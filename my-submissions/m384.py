class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.shuffled = nums.copy()

    def reset(self) -> List[int]:
        self.shuffled = self.nums.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        indices = set(range(len(self.nums)))
        self.shuffled = []
        
        while indices :
            temp = random.choice(list(indices))
            self.shuffled.append(self.nums[temp])
            indices.remove(temp)
        return self.shuffled

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()