// https://leetcode.com/problems/palindrome-number/

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int one = 0;
        int two = x;

        while (two > 0) {
            one = 10 * one + two % 10;
            two /= 10;
        }

        return x == one;
    }
}