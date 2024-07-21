class Solution:
    def minChanges(self, n: int, k: int) -> int:
        counter = 0
        while n > 0 :
            if n % 2 == 0 and k % 2 == 1 :
                return -1
            elif n % 2 == 1 and k % 2 == 0 :
                counter += 1
            n //= 2
            k //= 2
        return -1 if k else counter