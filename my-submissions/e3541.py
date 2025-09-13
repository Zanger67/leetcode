class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = Counter(s)
        cons, vow = 0, 0
        for k, v in cnt.items() :
            if k in 'aeiou' and v > vow :
                vow = v
            elif k not in 'aeiou' and v > cons :
                cons = v
        return cons + vow