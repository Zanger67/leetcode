# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for s in strs :
            key = ''.join(sorted(s))

            if key in output :
                output[key].append(s)
            else :
                output[key] = [s]

        return [x for x in output.values()]