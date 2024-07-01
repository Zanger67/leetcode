class Solution {
    public boolean isValid(String s) {
        Stack<Character> temp = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[' || s.charAt(i) == '(' || s.charAt(i) == '{') {
                temp.add(s.charAt(i));
            } else if (s.charAt(i) == ']' || s.charAt(i) == ')' || s.charAt(i) == '}') {
                if (temp.isEmpty()) {
                    return false;
                } else {
                    switch (s.charAt(i)) {
                        case ']' :
                            if (temp.peek() != '[') {
                                return false;
                            }
                            break;
                        case '}' :
                            if (temp.peek() != '{') {
                                return false;
                            }
                            break;
                        case ')' :
                            if (temp.peek() != '(') {
                                return false;
                            }
                            break;
                        default :
                            return false;       
                    }

                    temp.pop();
                }
            }
        }

        return temp.isEmpty();
    }
}