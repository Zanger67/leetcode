// Around the [40, 50]% range runtime wise

class Solution {
    public int appendCharacters(String s, String t) {
        int pointerT = 0;

        for (Character c : s.toCharArray()) {
            if (c == t.charAt(pointerT)) {
                pointerT++;
            }
            if (pointerT == t.length()) {
                break;
            }
        }

        return t.length() - pointerT;
    }
}