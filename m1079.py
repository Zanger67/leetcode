class Solution:
    def dfs(self, tiles: List[int], used: List[int], used_sum: int) -> int :
        # Calculates the number of states using the multinomial coefficient
        # to avoid propogating to all cases
        if not tiles :
            return factorial(used_sum) // prod([factorial(x) for x in used])

        x = tiles.pop()
        output = self.dfs(tiles, used, used_sum)    # case: we don't use this value

        for i in range(1, x + 1) :                  # case: we use "i" number of this value
            used.append(i)
            output += self.dfs(tiles, used, used_sum + i)
            used.pop()
        tiles.append(x)

        return output

    def numTilePossibilities(self, tiles: str) -> int:
        return self.dfs(list(Counter(tiles).values()), [], 0) - 1