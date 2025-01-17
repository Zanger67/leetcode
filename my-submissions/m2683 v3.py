class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not(derived.count(1) % 2)