class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = re.findall('[aeiou]{1}', s)

        return (len(vowels) > 0)