class Solution:
    def sortVowels(self, s: str) -> str:
        b = 'AEIOUaeiou'
        base = {x: i for i, x in enumerate(b)}
        cnt = [0] * len(base)

        for c in s :
            if c in base :
                cnt[base[c]] += 1

        output = []
        i = 0

        for c in s :
            if c not in base :
                output.append(c)
                continue
            while i < len(cnt) and cnt[i] == 0 :
                i += 1
            output.append(b[i])
            cnt[i] -= 1

        return ''.join(output)