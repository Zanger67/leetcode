class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> cnt1 = new HashMap<>();
        HashMap<Integer, Integer> cnt2 = new HashMap<>();

        for (int i : nums1) {
            cnt1.put(i, cnt1.getOrDefault(i, 0) + 1);
        }

        for (int i : nums2) {
            cnt2.put(i, cnt2.getOrDefault(i, 0) + 1);
        }

        ArrayList<Integer> output = new ArrayList<>();
        for (Integer i : cnt1.keySet()) {
            for (int j = 0; j < Integer.min(cnt1.get(i), cnt2.getOrDefault(i, 0)); j++) {
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