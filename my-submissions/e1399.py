class Solution:
    def countLargestGroup(self, n: int) -> int:
        gps = Counter([sum(map(int, str(x))) for x in range(1, n + 1)])
        output = Counter(gps.values())
        return output[max(output.keys())]