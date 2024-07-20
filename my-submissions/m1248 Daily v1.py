class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        oddCounter = 0
        remainders = [0] * len(nums)
        for i in range(len(nums)) :
            if nums[i] % 2 == 1 :
                oddCounter += 1
                remainders[i] = 1

            nums[i] = oddCounter

        left, right = 0, 0

        counter = 0
        visited = set()
        toVisit = deque([(0, 0)])
        while toVisit :
            left, right = toVisit.popleft()

            if left >= len(nums) or right >= len(nums) :
                continue
            if (left, right) in visited :
                continue
            visited.add((left, right))

            odds = nums[right] - nums[left] + remainders[left]
            if odds == k :
                counter += 1
                toVisit.append((left + 1, right))
                toVisit.append((left, right + 1))
            
            elif odds < k :
                toVisit.append((left, right + 1))
            
            else :
                toVisit.append((left + 1, right))
        return counter