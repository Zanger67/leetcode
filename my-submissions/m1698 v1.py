# Inefficient brute force solution using high memory and sets but works

class Solution:
    def countDistinct(self, s: str) -> int:
        outputSet = set()
        def helper(sub: str):
            if sub in outputSet :
                return 
            outputSet.add(sub) 
            
            helper(sub[1:]) 
            helper(sub[:-1])

        helper(s)
        return len(outputSet) - 1
        
        
# Slightly less efficient option: 

# class Solution:
#     def countDistinct(self, s: str) -> int:
#         outputSet = set()
#         def helper(sub: str) -> int :
#             if sub in outputSet :
#                 return 0
#             outputSet.add(sub) 
            
#             return 1 + helper(sub[1:]) + helper(sub[:-1])

#         return helper(s) - 1
        