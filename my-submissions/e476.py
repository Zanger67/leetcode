class Solution:
    def findComplement(self, num: int) -> int:
        num = list(bin(num))
        mp = ['1', '0']

        for i, c in enumerate(num[2:], 2) :
            num[i] = mp[ord(c) - ord('0')]

        return int(''.join(num), 2)
