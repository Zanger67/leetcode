// https://leetcode.com/problems/score-of-a-string/?envType=daily-question&envId=2024-06-01

class Solution {
    public int scoreOfString(String s) {
        int output = 0;
        char[] temp = s.toCharArray();
        for (int i = 0; i < temp.length - 1; i++) {
            output += Math.abs((temp[i] - temp[i + 1]));
        } 

        return output;
    }
}