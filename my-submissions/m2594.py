class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        freq = Counter(ranks)
        left, right = 1, min(ranks) * cars * cars

        while left < right :
            midd = (left + right) // 2
            repped = sum(freq[rank] * int(sqrt(midd // rank)) for rank in freq)
            left, right = (midd + 1, right) if repped < cars else (left, midd)

        return left