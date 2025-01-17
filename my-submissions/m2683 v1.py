class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        orig_prev = 0

        for i, v in enumerate(derived) :
            orig_prev = v ^ orig_prev
        
        if orig_prev == 0 :
            return True
        
        orig_prev = 1

        for i, v in enumerate(derived) :
            orig_prev = v ^ orig_prev
        

        return orig_prev == 1