class Solution {
    public int numberOfSpecialSubstrings(String s) {
        int[] previousOccurances = new int[26];
        Arrays.fill(previousOccurances, -1);

        int left = 0;
        int output = 0;

        for (int i = 0; i < s.length(); i++) {
            int previousIndex = previousOccurances[s.charAt(i) - 'a'];
            int newVal = 1 + i - left;

            if (previousIndex != -1 && previousIndex >= left) {
                int shiftAmount = previousIndex - left + 1;
                left = previousIndex + 1;
                newVal -= shiftAmount;
            }

            previousOccurances[s.charAt(i) - 'a'] = i;
            output += newVal;
        }

        return output;

    }
}
