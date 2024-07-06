class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter(s[0])

        longest = 0
        left, right = 0, 0
        while right < len(s) :
            maxxChar = max(cnt, key=lambda x: cnt[x])
            sumOthers = sum([cnt[x] for x in cnt if x != maxxChar])

            if sumOthers > k :
                cnt[s[left]] -= 1
                left += 1

            else :
                longest = max(longest, sumOthers + cnt[maxxChar])
                right += 1
                if right < len(s) :
                    cnt[s[right]] += 1

        return longest