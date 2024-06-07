# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        singleStr = re.sub('[^A-Za-z0-9]', '', s).lower()

        for i in range(len(singleStr) // 2) :
            if not singleStr[i] == singleStr[len(singleStr) - i - 1] :
                return False 

        return True