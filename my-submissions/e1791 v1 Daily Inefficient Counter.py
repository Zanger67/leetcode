class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgeCounter = defaultdict(int)

        for edge in edges :
            edgeCounter[edge[0]] += 1
            edgeCounter[edge[1]] += 1
            
        return max([x for x in edgeCounter], key=lambda x:edgeCounter.get(x))
        