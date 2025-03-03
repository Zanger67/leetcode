class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        output = []

        pivot_occ_cnt = 0
        for num in nums :
            if num < pivot :
                output.append(num)
            elif num == pivot :
                pivot_occ_cnt += 1

        output.extend([pivot] * pivot_occ_cnt)

        for num in nums :
            if num > pivot :
                output.append(num)

        return output