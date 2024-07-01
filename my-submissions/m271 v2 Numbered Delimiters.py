# This is designed to split the strings by delimiter with a number preceding in
# order to track the string lengths

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join([(f'{len(s)}🍁{s}') for s in strs])
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        output = []

        indx = 0

        while indx < len(s) :
            delimIndx = s.find('🍁', indx)

            if delimIndx == -1 :
                break
            
            numChars = int(s[indx:delimIndx])
            indx = delimIndx + 1 + numChars
            output.append(s[delimIndx + 1 : indx])
        return output
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))