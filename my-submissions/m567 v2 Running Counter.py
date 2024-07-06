class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26

        if len(s1) > len(s2) :
            return False

        for c1, c2 in zip(s1, s2) :
            cnt1[ord(c1) - ord('a')] += 1
            cnt2[ord(c2) - ord('a')] += 1

        matches = [cnt1[x] == cnt2[x] for x in range(len(cnt1))].count(True)

        if matches == 26 :
            return True
        for cL, cR in zip(s2, s2[len(s1):]) :
            cnt2[ord(cL) - ord('a')] -= 1
            cnt2[ord(cR) - ord('a')] += 1

            if cL == cR :
                continue

            if cnt2[ord(cR) - ord('a')] == cnt1[ord(cR) - ord('a')] :
                matches += 1
            elif cnt2[ord(cR) - ord('a')] == cnt1[ord(cR) - ord('a')] + 1 :
                matches -= 1

            if cnt2[ord(cL) - ord('a')] == cnt1[ord(cL) - ord('a')] :
                matches += 1
            elif cnt2[ord(cL) - ord('a')] == cnt1[ord(cL) - ord('a')] - 1 :
                matches -= 1

            if matches == 26 :
                return True

        return False