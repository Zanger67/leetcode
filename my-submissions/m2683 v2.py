class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not reduce(xor, derived)