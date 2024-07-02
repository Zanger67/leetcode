class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        maxx = 0

        for i in range(len(nums)) :
            if i in visited :
                continue

            counter = 1
            curr = nums[i]
            while curr != i :
                counter += 1
                visited.add(curr)
                curr = nums[curr]
            maxx = max(maxx, counter)

        return maxx