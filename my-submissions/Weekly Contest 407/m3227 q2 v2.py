
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return re.search('[aeiou]{1}', s)