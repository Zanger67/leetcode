class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt_w1 = Counter(words1)
        cnt_w2 = Counter(words2)
        return sum(v == 1 and cnt_w2[k] == 1 for k, v in cnt_w1.items())
