class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n :
            return 1
        
        if n == 1 :
            return x
        
        if n < 0 :
            return 1 / self.myPow(x, -n)

        half = n // 2
        remainder = n - half * 2
        half = self.myPow(x, half)

        if remainder :
            return x * half * half
        
        return half * half