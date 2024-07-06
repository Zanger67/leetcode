class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:len(s1) - 1])

        for cL, cR in zip(s2, s2[len(s1) - 1 : len(s2)]) :
            cnt2[cR] += 1
            if cnt1 == cnt2 :
                return True
            cnt2[cL] -= 1

        return False