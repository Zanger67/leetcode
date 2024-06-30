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
            toVisitPriority = [1]
            toVisitSecondary = []

            while toVisitPriority or toVisitSecondary :
                curr = None
                fromPriority = False
                if toVisitPriority :
                    fromPriority = True
                    curr = toVisitPriority.pop()
                else :
                    curr = toVisitSecondary.pop()

                if curr in visited :
                    continue
                if fromPriority :
                    self.randafksf += 1

                visited.add(curr)

                for i in both[curr] :
                    toVisitPriority.append(i)
                for i in person[curr] :
                    toVisitSecondary.append(i)

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

        return totalEdges - edgesNeeded - 1

