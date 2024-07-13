class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1 == word2 :
            return True

        cnt1, cnt2 = Counter(word1), Counter(word2)
        freqCnt1, freqCnt2 = Counter(cnt1.values()), Counter(cnt2.values())

        if freqCnt1 == freqCnt2 and cnt1.keys() == cnt2.keys() :
            return True

        return False
