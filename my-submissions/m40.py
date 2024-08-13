class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort since if we add an index and it's greater,
        # then adding any index past that will also be greater
        candidates.sort()

        def helper(currTotal: int = 0,
                   currIndx: int = 0, 
                   valsSoFar: List[int] = [],
                   output: List[int] = []) -> List[int] :
            if currTotal == target :
                output.append(valsSoFar.copy())
                return output

            if currTotal > target :
                return output

            # Iterate through each next potential value till too big
            while currIndx < len(candidates) and candidates[currIndx] + currTotal <= target :
                # To avoid repeat combinations, jump past the group of same values
                startIndx, endIndx = currIndx, currIndx
                while endIndx < len(candidates) and candidates[endIndx] == candidates[startIndx] :
                    endIndx += 1

                for i in range(startIndx, endIndx) :
                    if currTotal + candidates[currIndx] > target :
                        break
                    valsSoFar.append(candidates[currIndx])
                    currTotal += candidates[currIndx]
                    helper(currTotal, endIndx, valsSoFar, output)

                # Remove the values since we're using the same valsSoFar pointer
                while valsSoFar and valsSoFar[-1] == candidates[currIndx] :
                    currTotal -= valsSoFar.pop()

                currIndx = endIndx
            return output

        return helper()
