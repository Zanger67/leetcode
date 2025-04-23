class Solution:
    def countLargestGroup(self, n: int) -> int:
        return (output := Counter(Counter([sum(map(int, str(x))) for x in range(1, n + 1)]).values()))[max(output.keys())]