# https://leetcode.com/problems/relative-sort-array/description/?envType=daily-question&envId=2024-06-11

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        arr2Set = set(arr2)
        output = []

        for i in arr2 :
            output.extend([i] * cnt.get(i))
            cnt.pop(i)
        
        for key in sorted(cnt.keys()) :
            output.extend([key] * cnt.get(key))

        return output
