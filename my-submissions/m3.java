class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxSoFar = 0;
        for (int i = 0; i < s.length() && s.length() - i > maxSoFar; i++) {
            int counter = 0;
            HashSet<Character> temp = new HashSet<>();
            for (int j = i; j < s.length(); j++) {
                if (temp.contains(s.charAt(j))) {
                    break;
                } else {
                    temp.add(s.charAt(j));
                }

                counter++;
            }

            if (maxSoFar < counter) {
                maxSoFar = counter;
            }
        }

        return maxSoFar;
    }
}