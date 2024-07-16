class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def combos(outputs: List[List[int]], 
                   current: List[int] = [], 
                   currentSum: int = 0, 
                   candidates: List[int] = candidates) -> None :
            if currentSum > target :
                return
            if currentSum == target :
                outputs.append(current.copy())
                return
            if not candidates :
                return

            hold = candidates.pop()
            combos(outputs, current, currentSum, candidates)
            currentSum += hold
            cnt = 0

            while currentSum <= target :
                current.append(hold)
                cnt += 1
                combos(outputs, current, currentSum, candidates)
                currentSum += hold

            for _ in range(cnt) :
                current.pop()
            candidates.append(hold)

        candidates.sort()
        output = []
        combos(output)

        return output
