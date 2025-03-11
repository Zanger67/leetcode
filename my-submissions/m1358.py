class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = -1
        output = 0

        for i, x in enumerate(s) :
            match x :
                case 'a' :
                    a = i
                case 'b' :
                    b = i
                case 'c' :
                    c = i

            if min(a, b, c) != -1 :
                output += 1 + min(a, b, c)

        return output