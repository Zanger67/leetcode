class Solution {
    public String customSortString(String order, String s) {
        int[] charCounter = new int[26];

        for (char c : s.toCharArray()) {
            charCounter[c - 'a']++;
        }

        StringBuilder sb = new StringBuilder();
        for (char c : order.toCharArray()) {
            for (int i = 0; i < charCounter[c - 'a']; i++) {
                sb.append(c);
            }
            charCounter[c - 'a'] = 0;
        }

        for (int i = 0; i < charCounter.length; i++) {
            while (charCounter[i] > 0) {
                sb.append((char) ('a' + i));
                charCounter[i]--;
            }
        }

        return sb.toString();
    }
}