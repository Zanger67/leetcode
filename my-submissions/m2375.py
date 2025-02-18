class Solution:
    # i defaults to -1 since the first value doesn't "satisfy" part of the pattern
    def dfs(self, pot_vals: List[int], pattern: str, i: int = -1, output: List[str] = None) -> bool | List[str] :
        if output is None :
            output = []
        if not pot_vals or i >= len(pattern):
            return output

        # Checks smallest values first for leftmost indices
        for j in range(len(pot_vals) - 1, -1, -1) :
            if not output or \
               (pot_vals[j] < output[-1] and pattern[i] == 'D') or \
               (pot_vals[j] > output[-1] and pattern[i] == 'I') :
                output.append(pot_vals.pop(j))
                nxt = self.dfs(pot_vals, pattern, i + 1, output)
                if nxt :
                    return nxt
                pot_vals.insert(j, output.pop())

        return False

    def smallestNumber(self, pattern: str) -> str:
        return ''.join(map(str, self.dfs(list(reversed(range(1, len(pattern) + 2))), pattern)))
