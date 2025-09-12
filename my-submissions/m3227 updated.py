class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return bool(re.search('[aeiou]{1}', s))