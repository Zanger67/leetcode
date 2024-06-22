class Solution {
    public int minProductSum(int[] nums1, int[] nums2) {
        int output = 0;

        Arrays.sort(nums1);
        Arrays.sort(nums2);

        for (int i = 0; i < nums1.length; i++) {
            output += nums1[i] * nums2[nums2.length - i - 1];
        }

        return output;
    }
}
