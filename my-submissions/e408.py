# This is NOT an easy question lmao
# It's not hard, it just has wayyyyy too many edge cases that can only be found via submitting sigh

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(word) == 1 :
            return abbr == word or abbr == '1'

        strs = [x for x in re.split(r'\d', abbr) if not x == '']
        vals = [x for x in re.findall(r'\d+', abbr) if not x == '']

        for i in vals:
            if i[0] == '0':
                return False

        if len(strs) == 0:
            return int(vals[0]) == len(word)

        index = 0
        strsIndex = 0
        valsIndex = 0
        currentlyStrs = word[0:len(strs[0])] == strs[0]

        while strsIndex < len(strs) or valsIndex < len(vals) :
            if currentlyStrs :
                if strsIndex >= len(strs) :
                    return False
                if word[index:index + len(strs[strsIndex])] == strs[strsIndex] :
                    index += len(strs[strsIndex])
                    strsIndex += 1
                    currentlyStrs = not currentlyStrs
                else :
                    return False
            else :
                if valsIndex >= len(vals) :
                    return False
                index += int(vals[valsIndex])
                valsIndex += 1
                if index > len(word) :
                    return False
                currentlyStrs = not currentlyStrs
        return len(word) == index
        