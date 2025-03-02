class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        return sorted(((output := {_id:_val for _id, _val in nums1}).update({_id: _val + output.get(_id, 0) for _id, _val in nums2}), output.items())[1])