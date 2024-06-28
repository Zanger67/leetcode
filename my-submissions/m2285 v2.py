class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnt = [0] * n
        for road in roads :
            cnt[road[0]] += 1
            cnt[road[1]] += 1
        cnt.sort()

        i = n
        output = 0

        while cnt and cnt[-1] > 0 :
            output += i * cnt.pop()
            i -= 1

        return output