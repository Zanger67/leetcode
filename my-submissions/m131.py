class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1 :
            return [[s]]
        
        output = []
        for i in range(1, len(s) + 1) :
            if s[0:i] == s[i-1::-1] :
                if i == len(s) :
                    output.append([s])
                    continue

                right = self.partition(s[i:])
                for r in right :
                    output.append([s[0:i]] + r)

        return output