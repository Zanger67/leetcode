# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/
# https://leetcode.com/contest/weekly-contest-401/

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k %= (2 * n - 2)
        if k >= n :
            return (n - 1) - (k - (n - 1))
        return k
        