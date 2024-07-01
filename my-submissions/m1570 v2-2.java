class SparseVector {
    
    private HashMap<Integer, Integer> vals = new HashMap<>();
    SparseVector(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                vals.put(i, nums[i]);
            }
        }
    }
    
	// Return the dotProduct of two sparse vectors
    public int dotProduct(SparseVector vec) {
        int output = 0;
        for (Integer i : vals.keySet()) {
            if (vec.vals.containsKey(i)) {
                output += vec.vals.get(i) * vals.get(i);
            }
        }
        return output;
    }
}

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1 = new SparseVector(nums1);
// SparseVector v2 = new SparseVector(nums2);
// int ans = v1.dotProduct(v2);