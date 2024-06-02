# https://leetcode.com/problems/reverse-string/description/?envType=daily-question&envId=2024-06-02
# Daily question

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s) // 2) :
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]