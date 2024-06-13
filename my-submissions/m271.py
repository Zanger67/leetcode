# https://leetcode.com/problems/encode-and-decode-strings/description/

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return '🍁'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('🍁')
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))