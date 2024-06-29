# We can basically do levelorder traversals starting at 0, 1, 2,...
# with compensating recursive calls

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        directAncestors = [set() for _ in range(n)]
        visited = [False] * n

        # Add immediate predecessors
        for source, target in edges :
            directAncestors[target].add(source)


        # Helper method that merges a node's ancestor set with 
        # any ancestor's ancestor set
        def helper(currentIndx: int) -> None :
            if visited[currentIndx] :
                return

            visited[currentIndx] = True
            if not directAncestors[currentIndx] : # is oldest ancestor
                return
            
            mergeSet = set()
            for item in directAncestors[currentIndx] :
                helper(item) # make sure it's been initialized first
                mergeSet |= directAncestors[item]
            
            directAncestors[currentIndx] |= mergeSet

        for i in range(n) :
            if not visited[i] :
                helper(i)
            

        return [sorted(list(x)) for x in directAncestors]