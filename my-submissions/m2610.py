class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        maxx = max(cnt.values())
        output = []
        for i in range(maxx) :
            output.append([])
        for i in cnt :
            for j in range(cnt.get(i)) :
                output[j].append(i)

        return output
