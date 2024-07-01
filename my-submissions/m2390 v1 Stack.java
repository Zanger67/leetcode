// Pretty good due to stringbuilder but the lack of a way to directly go to the result from stack
// is kinda annoying lol

class Solution {
    public String removeStars(String s) {
        Stack<Character> output = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '*') {
                output.pop();
            } else {
                output.push(c);
            }
        }

        Character[] temp = new Character[output.size()];
        temp = output.toArray(temp);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < temp.length; i++) {
            sb.append(temp[i]);
        }
        

        return sb.toString();
    }
}