class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[i for i in range(len(str1) + 1)]] + \
             [[i] + [None] * len(str1) for i in range(1, 1 + len(str2))]
        dp[0][0] = 0

        for i, ci in enumerate(str2, 1) :
            for j, cj in enumerate(str1, 1) :
                dp[i][j] = min(
                        dp[i - 1][j], 
                        dp[i][j - 1],
                        dp[i - 1][j - 1] if ci == cj else inf   # if same letter
                    ) + 1

        output = []
        r, c = len(dp) - 1, len(dp[0]) - 1

        while r > 0 and c > 0 :
            if dp[r][c] == dp[r - 1][c - 1] + 1 and str1[c - 1] == str2[r - 1]:
                c -= 1
                r -= 1
                output.append(str1[c])
                continue

            if dp[r][c - 1] == dp[r][c] - 1 :
                c -= 1
                output.append(str1[c])
                continue

            r -= 1
            output.append(str2[r])

        output.extend((reversed(str1[:c])))
        output.extend((reversed(str2[:r])))

        return ''.join(reversed(output))