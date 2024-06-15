class Solution:
    def decodeString(self, s: str) -> str:
        output = []
        currentIndx = 0

        while currentIndx < len(s) :
            if s[currentIndx].isnumeric() :
                numStart = currentIndx
                while s[currentIndx].isnumeric() :
                    currentIndx += 1

                bracketStart = currentIndx
                num = int(s[numStart:bracketStart])

                numOpeners = 1
                while numOpeners > 0 :
                    currentIndx += 1
                    
                    if s[currentIndx] == '[' :
                        numOpeners += 1
                    elif s[currentIndx] == ']' :
                        numOpeners -= 1

                ending = currentIndx
                middle = self.decodeString(s[bracketStart + 1: ending])

                output.extend(num * [middle])
                currentIndx += 1
            else :
                output.append(s[currentIndx])
                currentIndx += 1
        
        return ''.join(output)