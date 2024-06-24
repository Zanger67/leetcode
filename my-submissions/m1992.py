class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        output:List[List[int]] = []

        for r in range(len(land)) :
            for c in range(len(land[0])) :
                if land[r][c] \
                    and (r == 0 or not land[r - 1][c]) \
                    and (c == 0 or not land[r][c - 1]) :
                    output.append([r, c, r, c])
                    
                    rRight, cRight = r, c
                    while True :
                        if rRight >= len(land) or land[rRight][c] == 0 :
                            output[-1][2] = rRight - 1
                            break
                        rRight += 1
                    while True :
                        if cRight >= len(land[0]) or land[r][cRight] == 0 :
                            output[-1][3] = cRight - 1
                            break
                        cRight += 1
        
        return output