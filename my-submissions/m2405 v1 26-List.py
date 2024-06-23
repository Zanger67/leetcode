# Wanted to see if a 26-long list being reset each time would be faster
# than a hashmap

class Solution:
    def partitionString(self, s: str) -> int:
        current: List[bool] = [False] * 26

        counter = 1
        for c in s :
            if current[ord(c) - ord('a')] :
                counter += 1
                current = [False] * 26
                current[ord(c) - ord('a')] = True
            
            else :
                current[ord(c) - ord('a')] = True

        return counter