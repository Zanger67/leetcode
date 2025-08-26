class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        cnt = 0
        val = mat[0][0]
        r_curr = 0
        c_currs = [0] * len(mat)

        while cnt < len(mat) :
            if c_currs[r_curr] >= len(mat[0]) : 
                return -1

            val_curr = mat[r_curr][c_currs[r_curr]]

            if val_curr == val :
                cnt += 1
                r_curr = (r_curr + 1) % len(mat)
                continue

            if val_curr < val :
                c_currs[r_curr] += 1
                continue

            # if greater than current test val so we have a new "lowest common" candidate
            cnt = 0
            val = mat[r_curr][c_currs[r_curr]]

        return val