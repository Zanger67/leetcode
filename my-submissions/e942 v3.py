class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        return [(l := 0 if 'l' not in locals() else l + 1) if c == 'I' else (r := len(s) if 'r' not in locals() else r - 1) for c in s] + [l + 1 if 'l' in locals() else r - 1]