class Solution {
    public int maxResult(int[] nums, int k) {
        ArrayDeque<Integer> vals = new ArrayDeque<Integer>();
        ArrayDeque<Integer> indices = new ArrayDeque<Integer>();

        vals.add(nums[0]);
        indices.add(0);

        for (int i = 1; i < nums.length; i++) {
            while (indices.getLast() < i - k) {
                indices.removeLast();
                vals.removeLast();
            }
            int val = vals.getLast() + nums[i];
            while (!indices.isEmpty() && (indices.getFirst() < i - k || vals.getFirst() < val)) {
                indices.removeFirst();
                vals.removeFirst();
            }
            indices.addFirst(i);
            vals.addFirst(val);
        }

        return vals.getFirst();
    }
}