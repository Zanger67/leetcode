 class Solution {
    public int longestSubarray(int[] nums, int limit) {
        int output = 0;

        PriorityQueue<Pair<Integer, Integer>> max = new PriorityQueue<>(Comparator.comparing(Pair::getValue)); // * -1
        PriorityQueue<Pair<Integer, Integer>> min = new PriorityQueue<>(Comparator.comparing(Pair::getValue)); // Default min 

        int indxLeft   = 0;
        int indexRight = 0;

        while (indexRight < nums.length) {
            max.add(new Pair<>(indexRight, -1 * nums[indexRight]));
            min.add(new Pair<>(indexRight, nums[indexRight]));

            while (max.peek().getKey() < indxLeft) {
                max.remove();
            }
            while (min.peek().getKey() < indxLeft) {
                min.remove();
            }

            int maxVal = -1 * max.peek().getValue();
            int maxIndx = max.peek().getKey();

            int minVal = min.peek().getValue();
            int minIndx = min.peek().getKey();
            
            if (maxVal - minVal > limit) {
                if (maxIndx > minIndx) {
                    indxLeft = minIndx + 1;
                    continue;
                } else {
                    indxLeft = maxIndx + 1;
                    continue;
                }
            } else {
                if (indexRight - indxLeft + 1 > output) {
                    output = indexRight - indxLeft + 1;
                }
                indexRight++;
            }
        }

        return output;
    }
}