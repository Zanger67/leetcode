class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        minn, maxx = 0, 0
        output = [0] + [(maxx := maxx + 1) if c == 'I' else (minn := minn - 1) for c in s]
        return [x - minn for x in output]