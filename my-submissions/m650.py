class Solution:
    def minSteps(self, n: int) -> int:
        self.val = inf

        def propogate(currLen: int = 1, copyLen: int = 0, steps: int = 0) -> None :
            if currLen == n :
                if self.val > steps :
                    self.val = steps
                return

            if currLen != copyLen and currLen + currLen <= n:
                propogate(currLen, currLen, steps + 1)

            if copyLen != 0 and copyLen + currLen <= n :
                propogate(currLen + copyLen, copyLen, steps + 1)

        propogate()
        return self.val
