class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        letters = set()
        left    = 0
        output  = 0

        for c in s :
            if c in letters :
                while s[left] != c :
                    letters.remove(s[left])
                    left += 1
                left += 1
            letters.add(c)

            while len(letters) > k :
                letters.remove(s[left])
                left += 1

            if len(letters) == k :
                output += 1

        return output