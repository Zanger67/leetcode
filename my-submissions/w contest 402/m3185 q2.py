class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = Counter([x % 24 for x in hours])

        '''
        0
        1 23
        2 22
        3 21
        ...
        10 14
        11 13
        12
        '''

        vals = []
        vals.append(cnt.get(0, 0) * (cnt.get(0, 0) - 1) // 2)
        vals.append(cnt.get(12, 0) * (cnt.get(12, 0) - 1) // 2)

        for x in range(1, 12) : # [1, 11]
            vals.append(cnt.get(x, 0) * cnt.get(24 - x, 0))


        return sum(vals)
