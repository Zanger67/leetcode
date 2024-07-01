class Solution {
    public int minimumBuckets(String hamsters) {
        int counter = 0;

        for (int i = 0; i < hamsters.length(); i++) {
            if (hamsters.charAt(i) != 'H') {
                continue;
            }
            counter++;
            
            if ((i == hamsters.length() - 1 || hamsters.charAt(i + 1) == 'H') && (i == 0 || hamsters.charAt(i - 1) == 'H')) {
                return -1;
            }
            if (i != hamsters.length() - 1 && hamsters.charAt(i + 1) != 'H') {
                i += 2;
            }
        }

        return counter;
    }
}