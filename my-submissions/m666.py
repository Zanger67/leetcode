class Solution:
    def pathSum(self, nums: List[int]) -> int:
        vals = {}
        leaves = set()
        for num in nums :
            depth = num // 100
            pos = (num // 10) % 10
            val = num % 10

            indx = (depth, pos)
            parentIndx = (depth - 1, (pos + 1) // 2)
            leaves.add(indx)
            
            if parentIndx in leaves :
                leaves.remove(parentIndx)
                vals[indx] = vals[parentIndx] + val
            elif parentIndx in vals :
                vals[indx] = vals[parentIndx] + val
            else :
                vals[indx] = val

        output = 0
        for leaf in leaves :
            output += vals[leaf]

        return output
