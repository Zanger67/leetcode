class Solution:
    def minimumKeypresses(self, s: str) -> int:
        output = 0
        cnt = Counter(s)
        mapped = 9

        for v in sorted(cnt.values(), reverse=True) :
            cost = mapped // 9
            output += cost * v
            mapped += 1

        return output