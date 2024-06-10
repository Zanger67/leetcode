// https://leetcode.com/problems/count-number-of-homogenous-substrings/description/

class Solution {
    public int countHomogenous(String s) {
        int leftIndx = 0;
        char leftChar = s.charAt(0);

        long output = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != leftChar) {
                leftChar = s.charAt(i);
                output += helper(i - leftIndx);
                output %= (1000000000 + 7);
                leftIndx = i;
            }
        }
        output += helper(s.length() - leftIndx);
        output %= (1000000000 + 7);

        return (int) output;
    }
    public long helper(long numChars) {
        return (1 + numChars) * numChars / 2;
    }
}