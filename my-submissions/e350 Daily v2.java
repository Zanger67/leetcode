class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> cnt = new HashMap<>();

        for (int i : nums1) {
            cnt.put(i, cnt.getOrDefault(i, 0) + 1);
        }

        ArrayList<Integer> output = new ArrayList<>();
        for (int i : nums2) {
            if (cnt.getOrDefault(i, 0) > 0) {
                cnt.put(i, cnt.get(i) - 1);
                output.add(i);
            }
        }

        int[] outputArr = new int[output.size()];
        for (int i = 0; i < output.size(); i++) {
            outputArr[i] = output.get(i);
        }

        return outputArr;
    }
}