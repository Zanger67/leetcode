class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        # Generate trie
        trie = {}
        for cost, word in zip(costs, words) :
            curr = trie
            for c in word :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
            # If identical word exists, use smallest cost
            curr[False] = min(curr.get(False, inf), cost)

        # Dynamic Programming array
        dp = [0] + [inf] * len(target)

        # Iterate through each 
        for i in range(len(target)) :
            curr = trie
            offset = 0
            while i + offset < len(target) and target[i + offset] in curr  :
                curr = curr[target[i + offset]]
                offset += 1

                # Word ends
                if False in curr :
                    dp[i + offset] = min(dp[i + offset], dp[i] + curr[False])

        # -1 if end was not reachable
        return -1 if dp[-1] == inf else dp[-1] 
