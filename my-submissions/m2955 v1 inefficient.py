class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        chars = [Counter()] + [None for _ in range(len(s))]

        for i, c in enumerate(s, 1) :
            chars[i] = chars[i - 1] + Counter(c)

        output = []
        for q in queries :
            cnt = q[1] - q[0] + 1
            diffs = chars[q[1] + 1] - chars[q[0]]
            for k, v in diffs.items() :
                cnt += comb(v, 2)
            output.append(cnt)

        return output
