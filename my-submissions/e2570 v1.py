class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        output = {_id:_val for _id, _val in nums1}
        output.update({_id: _val + output.get(_id, 0) for _id, _val in nums2})
        return sorted([tuple(x) for x in output.items()])