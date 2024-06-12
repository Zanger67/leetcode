// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Boolean> stk = new Stack<>();

        int counter = 0;
        for (Character c : s.toCharArray()) {
            if (c == '(') {
                stk.push(true);
            } else if (stk.size() > 0 && stk.peek()) {
                stk.pop();
            } else {
                counter++;
            }
        }
        counter += stk.size();
        return counter;
    }
}