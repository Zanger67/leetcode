class Solution:
    def numTeams(self, rating: List[int]) -> int:
        valsLessThan = [0] * len(rating)
        valsGreaterThan = valsLessThan.copy()
        count = 0

        for right in range(len(rating)) :
            for mid in range(right) :
                # a < b < c case
                if rating[mid] < rating[right] :
                    count += valsLessThan[mid]
                    valsLessThan[right] += 1
                # a > b > c case since UNIQUE ratings only
                else :
                    count += valsGreaterThan[mid]
                    valsGreaterThan[right] += 1
        return count
