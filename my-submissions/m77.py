# Manual version to demonstrate understanding

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currentList = []
        self.outputCombos = []

        def helper(n: int, k: int, curr: [], remaining: []) :
            if len(curr) == k :
                self.outputCombos.append(curr.copy())
                return

            if not remaining :
                return

            val = remaining.pop()
            helper(n, k, curr, remaining)
            curr.append(val)
            helper(n, k, curr, remaining)
            curr.pop()
            remaining.append(val)

        helper(n, k, currentList, list(range(1, n + 1)))
        return self.outputCombos