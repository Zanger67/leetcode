class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        is_beaut = lambda x: all(int(k) == v for k, v in Counter(str(x)).items())
        n += 1
        while not is_beaut(n) :
            n += 1
        return n
