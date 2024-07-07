class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        wordToCost = {}
        for w, c in zip(words, costs) :
            if w in wordToCost and wordToCost[w] <= c :
                continue
            wordToCost[w] = c

        words = sorted(list(set(words)), key=lambda x: len(x))
        maxWrd = len(words) - 1

        dp = [0] + [inf] * len(target)

        for i in range(len(target)) :
            while maxWrd >= 0 and len(words[maxWrd]) > len(target) - i :
                maxWrd -= 1
            if maxWrd < 0 :
                break

            for word in words[:maxWrd + 1] :
                if word == target[i:i+len(word)] :
                    dp[i + len(word)] = min(dp[i + len(word)], dp[i] + wordToCost[word])
        
        return -1 if dp[-1] == inf else dp[-1] 
