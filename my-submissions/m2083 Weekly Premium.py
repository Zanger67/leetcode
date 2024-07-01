class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = Counter(s)
        output = len(s)

        for key in counter :
            if counter.get(key, 0) > 1 :
                output += (counter.get(key, 0)) * (counter.get(key, 0) - 1) // 2
        
        return output
