// Saw this solution and tried it myself and oh my is it elegant. Beautiful solution.

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] output = new int[temperatures.length];

        int currentMax = 0;
        for (int i = temperatures.length - 1; i >= 0; i--) {
            if (temperatures[i] >= currentMax) {    // default 0
                currentMax = temperatures[i];
                continue;
            }

            int offset = 1;
            while (temperatures[i] >= temperatures[i + offset]) {
                offset += output[i + offset];
            }
            output[i] = offset;
        }

        return output;
    }
}