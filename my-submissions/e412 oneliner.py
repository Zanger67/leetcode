# https://leetcode.com/problems/fizz-buzz/description/

# Cause funny hehe

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else str(x) for x in range(1, n + 1)]