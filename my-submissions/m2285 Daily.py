class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnt = Counter([roads[x // 2][x % 2] for x in range(len(roads) * 2)])
        validVals = sorted(list(cnt.values()))

        i = n
        output = 0

        while validVals :
            output += i * validVals.pop()
            i -= 1

        return output