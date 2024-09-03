class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def helper(curr, k: int) -> int :
            if not k :
                return curr

            newCurr = 0
            while curr :
                newCurr += curr % 10
                curr //= 10
            return helper(newCurr, k - 1)

        newCurr = 0
        for c in s :
            if ord(c) - ord('a') + 1 >= 10 :
                newCurr = 100 * newCurr + ord(c) - ord('a') + 1
            else :
                newCurr = 10 * newCurr + ord(c) - ord('a') + 1

        return helper(newCurr, k)
