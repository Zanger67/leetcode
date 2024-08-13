class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.cases = [(1, 9), (3, 7),
                      (1, 3), (4, 6), (7, 9),
                      (1, 7), (2, 8), (9, 3),]

        def dfs(prev: List[int], nxt: Set[int], minn: int, maxx: int) -> int :
            output = 0
            if minn <= len(prev) <= maxx :
                output += 1
            if not nxt or len(prev) >= maxx :
                return output


            temp = nxt.copy()
            for i in temp :
                if prev and ((prev[-1], i) in self.cases or (i, prev[-1]) in self.cases):
                    if (prev[-1] + i) // 2 not in prev :
                        continue

                nxt.remove(i)
                prev.append(i)
                output += dfs(prev, nxt, m, n)
                nxt.add(prev.pop())

            return output

        return dfs([], set([1,2,3,4,5,6,7,8,9]), m, n)
