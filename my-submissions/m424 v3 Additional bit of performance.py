class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter(s[0])

        longest = min(k, len(s))
        left, right = 0, 0
        while right < len(s) :
            if right - left + 1 <= longest :
                right += 1
                if right < len(s) :
                    cnt[s[right]] += 1
                continue

            maxxChar = max(cnt, key=lambda x: cnt[x])
            sumOthers = sum([cnt[x] for x in cnt if x != maxxChar])

            if sumOthers > k :
                cnt[s[left]] -= 1
                left += 1

            else :
                longest = right - left + 1
                right += 1
                if right < len(s) :
                    cnt[s[right]] += 1

        return longest