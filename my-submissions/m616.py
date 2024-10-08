# Identical to 758

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        trie = {}

        for word in words :
            curr = trie
            for c in word :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]

            curr[False] = True
        
        # Find intervals that need to be bolded
        intervals = []
        curr = {}
        for i, c in enumerate(s) :
            curr[i] = trie
            keys = list(curr.keys())
            for key in keys :
                if False in curr[key] :
                    intervals.append((key, i))
                
                if c not in curr[key] :
                    curr.pop(key)
                    continue
                
                curr[key] = curr[key][c]

        for i, branch in curr.items() :
            if False in branch :
                intervals.append((i, len(s)))

        intervals.sort(key=lambda x: x[0])

        # merging intervals
        output = []
        if intervals :
            output.append(s[:intervals[0][0]])
        
        indx = 0
        while indx < len(intervals) :
            left, right = intervals[indx]
            indx += 1

            while indx < len(intervals) and intervals[indx][0] <= right :
                if intervals[indx][1] > right :
                    right = intervals[indx][1]
                indx += 1

            output.append('<b>')
            output.append(s[left:right])
            output.append('</b>')
            
            if indx < len(intervals) :
                output.append(s[right:intervals[indx][0]])
        if intervals :
            output.append(s[right:])
        else :
            output.append(s)

        return ''.join(output)