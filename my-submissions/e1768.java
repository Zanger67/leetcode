class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();

        int indx1 = 0;
        int indx2 = 0;
        for (; indx1 < word1.length() && indx2 < word2.length(); indx1++, indx2++) {
            sb.append(word1.charAt(indx1));
            sb.append(word2.charAt(indx2));
        }

        sb.append(word1.substring(indx1));
        sb.append(word2.substring(indx2));

        return sb.toString();
    }
}