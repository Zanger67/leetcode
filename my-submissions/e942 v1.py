class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        minn, maxx = 0, 0
        output = [0]
        for c in s :
            if c == 'I' :
                output.append(maxx := maxx + 1)
            else :
                output.append(minn := minn - 1)
        return [x - minn for x in output]