// https://leetcode.com/problems/removing-stars-from-a-string/

// 80-90% region

class Solution {
    public String removeStars(String s) {
        ArrayDeque<Character> output = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (c == '*') {
                output.removeLast();
            } else {
                output.addLast(c);
            }
        }

        StringBuilder sb = new StringBuilder();

        while (!output.isEmpty()) {
            sb.append(output.pop());
        } 

        return sb.toString();
    }
}