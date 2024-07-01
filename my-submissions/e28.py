class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try :
            return haystack.index(needle)
        except Exception as e:
            return -1