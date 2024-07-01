# Similar to the previous v2 version but optimized after recognizing the lack of need for
# two independent sets

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for i in range(len(nums)) :
            if nums[i] :
                self.nums[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0
        
        for i in self.nums.keys() :
            if i in vec.nums.keys() :
                output += vec.nums[i] * self.nums[i]
                
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)