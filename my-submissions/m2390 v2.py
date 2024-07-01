# Much faster 95% region

class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        
        for i in s :
            if i == '*':
                output.pop()
            else:
                output.append(i)

        return ''.join(output)