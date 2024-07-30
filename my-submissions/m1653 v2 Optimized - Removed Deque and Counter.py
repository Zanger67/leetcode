class Solution:
    def minimumDeletions(self, s: str) -> int:
        counter = 0
        As = s.count('a')
        Bs = len(s) - As

        left, right = 0, len(s) - 1

        while left < right :
            if s[left] == 'a' :
                left += 1
                As -= 1
                continue
            if s[right] == 'b' :
                right -= 1
                Bs -= 1
                continue

            # which is blocking the least
            counter += 1
            if As > Bs :
                Bs -= 1
                left += 1
            else :
                As -= 1
                right -= 1

        return counter