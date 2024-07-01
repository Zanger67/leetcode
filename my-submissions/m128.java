class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> vals = new HashSet<>();

        for (int n : nums) {
            vals.add(n);
        }

        int maxCounter = 0;
        for (int n : vals) {
            if (vals.contains(n - 1)) {
                continue;
            }

            int counter = 1;
            while (vals.contains(n + counter)) {
                counter++;
            }

            if (counter > maxCounter) {
                maxCounter = counter;
            }

        }
        return maxCounter;
    }
}