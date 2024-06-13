# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for s in strs :
            cnt = [0] * 26
            for c in s :
                cnt[ord(c) - ord('a')] += 1
            cnt = tuple(cnt)
            
            if cnt in output :
                output[cnt].append(s)
            else :
                output[cnt] = [s]

        return [x for x in output.values()]