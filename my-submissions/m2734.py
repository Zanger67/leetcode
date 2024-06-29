class Solution:
    def smallestString(self, s: str) -> str:
        substringStarted  = False
        substringModified = False
        output = []

        for i, c in enumerate(s) :
            if substringStarted :
                if c == 'a' :
                    output.append(s[i:])
                    break
                else :
                    output.append(chr(ord(c) - 1))
            elif c != 'a' :
                substringModified = True
                substringStarted = True
                output.append(chr(ord(c) - 1))
            else :
                output.append(c)

        if not substringModified :
            output[-1] = 'z'

        return ''.join(output)