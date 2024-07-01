class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        vals = []
        
        push, pop = 0, 0
        while push < len(pushed) or pop < len(popped) :
            if vals and pop < len(popped) and popped[pop] == vals[-1] :
                pop += 1
                vals.pop()
            elif push < len(pushed) :
                vals.append(pushed[push])
                push += 1
            else : # no more to push and can't pop
                return False
        return True