// Not that good of a runtime

class Solution {
    public int[] findErrorNums(int[] nums) {
        int intendedSum = ((1 + nums.length) * nums.length) / 2;
        int actualSum = 0;
        HashSet<Integer> seenSet = new HashSet<>();
        int repeat = -1;
        for (int i: nums) {
            actualSum += i;
            
            if (seenSet.contains(i)) {
                repeat = i;
            }

            seenSet.add(i);
        }

        return new int[]{repeat, (repeat + intendedSum - actualSum)};
    }
}