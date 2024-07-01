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