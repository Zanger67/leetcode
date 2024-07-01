class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> previousMaxes = new Stack<>();  // Schema (temp, indx)

        int[] output = new int[temperatures.length];

        for (int i = temperatures.length - 1; i >= 0; i--) {
            while (!previousMaxes.isEmpty()) {
                if (previousMaxes.peek()[0] > temperatures[i]) {
                    output[i] = previousMaxes.peek()[1] - i;
                    break;
                }
                previousMaxes.pop();
            }
            previousMaxes.push(new int[] {temperatures[i], i});
        }

        return output;
    }
}