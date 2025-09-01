class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        # Min heap not including 100% ratios since
        # their ratios wouldn't change
        # (-1 * amount of ratio gain, total students, passing students)
        hp = [
            ((passing / tot - (passing + 1) / (tot + 1)), tot, passing) 
            for passing, tot in classes 
            if tot != passing
        ]
        heapify(hp)

        while hp and extraStudents :
            _, tot, passing = heappop(hp)

            tot += 1
            passing += 1
            heappush(hp, ((passing / tot - (passing + 1) / (tot + 1)), tot, passing))
            extraStudents -= 1

        return (sum(passing / tot for _, tot, passing in hp) + (len(classes) - len(hp))) / len(classes)