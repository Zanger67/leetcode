class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def helper(r: int, c: int, voidIt: bool) -> bool :
            if not (0 <= r < len(grid1)) or not (0 <= c < len(grid1[0])) :
                return True

            if not grid2[r][c] :
                return True

            grid2[r][c] = 0

            if not grid1[r][c] or voidIt :
                helper(r, c + 1, True)
                helper(r, c - 1, True)
                helper(r + 1, c, True)
                helper(r - 1, c, True)

                return False

            temp = helper(r, c + 1, False) 
            temp &= helper(r, c - 1, False)
            temp &= helper(r + 1, c, False)
            temp &= helper(r - 1, c, False)
            return temp 

        counter = 0
        for r in range(len(grid1)) :
            for c in range(len(grid1[0])) :
                if grid2[r][c] and helper(r, c, False) :
                    counter += 1

        return counter