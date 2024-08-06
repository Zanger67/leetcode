class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = sorted([f for f in Counter(word).values()])
        output = 0

        for i in range(len(cnt)) :
            output += cnt[-i - 1] * (ceil((i + 1) / 8))
        
        return output