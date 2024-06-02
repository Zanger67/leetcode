// https://leetcode.com/problems/removing-stars-from-a-string/

// 85-90% region!

class Solution {
    public String removeStars(String s) {
        StringBuilder sb = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c == '*') {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(c);
            }
        }
        
        return sb.toString();
    }
}