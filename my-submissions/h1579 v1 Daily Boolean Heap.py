''' Instinct/Notes
    In essence double prims where yuo always select the type 3s if present
    and not redundant?
'''

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        totalEdges = len(edges)
        bothEdges = 0
        aliceEdges = 0
        bobEdges = 0

        both = defaultdict(set)
        alice = defaultdict(set)
        bob = defaultdict(set)

        for tp, a, b in edges :
            match tp :
                case 1 :
                    # These ifs avoid duplicates
                    aliceEdges += 1
                    alice[a].add(b)
                    alice[b].add(a)
                case 2 :
                    bobEdges += 1
                    bob[a].add(b)
                    bob[b].add(a)
                case 3 :
                    if a not in both or b not in both:
                        bothEdges += 1
                    both[a].add(b)
                    both[b].add(a)

        if min(aliceEdges, bobEdges) + bothEdges < n - 1 :
            return -1

        def helper(both: dict, person: dict) -> Set[int] :
            visited = set()
            toVisit = [(True, 1)] # heap [isPerson, node]

            while toVisit :
                tp, node = heapq.heappop(toVisit)
                if node in visited :
                    continue
                
                visited.add(node)
                if not tp :
                    self.randafksf += 1
                
                for i in both[node] :
                    heapq.heappush(toVisit, (False, i))
                for i in person[node] :
                    heapq.heappush(toVisit, (True, i))

            return visited

        self.randafksf = 0
        outputAlice = helper(both, alice)
        if len(outputAlice) != n :
            return -1

        outputBob = helper(both, bob)
        if len(outputBob) != n :
            return -1
        
        # Note: |Edges| = |Nodes| - 1 in an MST
        edgesNeeded = 2 * n - 2
        edgesNeeded -= self.randafksf // 2

        return totalEdges - edgesNeeded

