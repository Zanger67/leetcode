class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()

        left, right = 0, 0
        maxFreq = 0
        for right in range(len(s)) :
            cnt[s[right]] += 1
            maxFreq = max(maxFreq, cnt[s[right]])
            
            if right - left + 1 - maxFreq > k :
                cnt[s[left]] -= 1
                left += 1

        return right - left + 1