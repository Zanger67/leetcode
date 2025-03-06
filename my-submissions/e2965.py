class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cnt = Counter()
        for g in grid :
            cnt.update(g)

        return [[k for k, v in cnt.items() if v == 2][0],
                [x for x in range(1, len(grid) ** 2 + 1) if x not in cnt][0]]