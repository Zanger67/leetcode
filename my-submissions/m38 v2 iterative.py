class Solution:
    def countAndSay(self, n: int) -> str:
        output = "1"
        for _ in repeat(None, n - 1) :
            curr, output = output, []
            prev, cnt    = None, 0
            for c in curr + "#" :
                if c == prev :
                    cnt += 1
                    continue
                if prev is not None :
                    output.extend([str(cnt), prev])
                prev, cnt = c, 1
            output = ''.join(output)
        return output