# Notably more efficient amortized & better space efficiency if highly sparse
# THIS IN EFFECT IS SIMILAR TO THE INDEX-PAIRS METHOD

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for i in range(len(nums)) :
            if nums[i] :
                self.nums[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0
        
        selfIndicies = sorted(self.nums.keys())
        vecIndicies = sorted(vec.nums.keys())

        while selfIndicies and vecIndicies :
            if selfIndicies[-1] > vecIndicies[-1] :
                selfIndicies.pop()
            elif selfIndicies[-1] < vecIndicies[-1] :
                vecIndicies.pop()
            else :
                output += vec.nums[vecIndicies.pop()] * self.nums[selfIndicies.pop()]
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)