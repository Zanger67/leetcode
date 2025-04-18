class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 :
            return '1'

        n_min_1 = self.countAndSay(n - 1)
        output = []

        prev, cnt = None, 0
        for c in n_min_1 + "#" :        # '#' acts as a delimiter
            if c == prev :              #     to append the final block
                cnt += 1
            else :
                if prev is not None :
                    output.append(str(cnt))
                    output.append(prev)
                prev, cnt = c, 1

        return ''.join(output)