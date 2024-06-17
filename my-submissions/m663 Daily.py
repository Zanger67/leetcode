class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cRoot       = ceil(c ** .5)
        valsUpTo    = [x ** 2 for x in range(cRoot + 1)]
        
        left, right = 0, len(valsUpTo) - 1
        while left < right :
            summ = valsUpTo[left] + valsUpTo[right]

            if summ > c :
                right -= 1
            elif summ < c :
                left += 1
            else :
                return True

        return 2 * valsUpTo[left] == c