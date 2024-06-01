# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/

# Literally middle of the pact consistently [50, 70%]


class Solution:
    def numSplits(self, s: str) -> int:
        counter = 0

        left, right = {}, dict(Counter(list(s)))

        for i in s :
            left[i] = left.get(i, 0) + 1

            if right.get(i) == 1 :
                right.pop(i)
            else :
                right[i] = right.get(i) - 1

            if len(right.keys()) == len(left.keys()) :
                counter += 1

        return counter
            

