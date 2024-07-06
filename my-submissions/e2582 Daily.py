class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= 2 * (n - 1)     # Remove there and backs
        if time < n :
            return time + 1
        time -= n - 1
        return n - time