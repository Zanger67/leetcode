# https://leetcode.com/problems/clear-digits/

# Pretty bad contest due to server issues and lag to a point where submissions and
# feedback were taking 10+ minutes each...

# Last week's weekly contest was similar not with lag but with the servers being down 
# for the first 15 minutes ;-;;;;

class Solution:
    def clearDigits(self, s: str) -> str:
        output = list(s)

        lets = set(list('abcdefghijklmnopqrstuvwxyz'))
        nums = set(list('0123456789'))

        for i in range(len(output)) :
            if output[i] in nums:
                output[i] = ''
                for j in range(i - 1, -1, -1) :
                    if output[j] in lets :
                        output[j] = ''
                        break
        return ''.join(output)