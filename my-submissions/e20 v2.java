
class Solution {
    public boolean isValid(String s) {
        Stack<Character> temp = new Stack<>();

        for (Character c : s.toCharArray()) {
            switch (c) {
                case '[' :
                case '{' :
                case '(' :
                    temp.push(c);
                    break;
                case ']' :
                    if (temp.isEmpty() || temp.pop() != '[')
                        return false;
                    break;
                case '}' :
                    if (temp.isEmpty() || temp.pop() != '{')
                        return false;
                    break;
                case ')' :
                    if (temp.isEmpty() || temp.pop() != '(')
                        return false;
                    break;
                default:
                    break;
            }
        }

        return temp.isEmpty();
    }
}