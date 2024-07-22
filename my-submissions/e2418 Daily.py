class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x for x, h in sorted(zip(names, heights), key=lambda y: y[1], reverse=True)]