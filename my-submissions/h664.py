class Solution:
    def strangePrinter(self, s: str) -> int:
        newS = [s[0]]

        for i, c in enumerate(s[1:]) :
            if c != s[i] :
                newS.append(c)

        @cache
        def recurs(i: int = 0, j: int = len(newS) - 1) -> int :
            if i > j :
                return 0

            output = 1 + recurs(i + 1, j)
            for k in range(i + 1, j + 1) :
                if newS[i] == newS[k] :
                    output = min(output, recurs(i, k - 1) + recurs(k + 1, j))

            return output

        return recurs()
