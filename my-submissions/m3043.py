class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}

        for s in arr1 :
            curr = trie
            for c in str(s) :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
            curr[False] = True
        
        maxx = 0
        for s in arr2 :
            curr = trie
            counter = 0
            for c in str(s) :
                if c not in curr :
                    break
                counter += 1
                curr = curr[c]
            maxx = max(maxx, counter)

        return maxx