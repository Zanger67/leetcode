class Solution:
    def makeFancyString(self, s: str) -> str:
        output = []
        prev, cnt = None, 0
        for c in s :
            if c == prev :
                cnt += 1
            else :
                cnt = 1
                prev = c
            if cnt >= 3 :
                continue
            output.append(c)
        return ''.join(output)
