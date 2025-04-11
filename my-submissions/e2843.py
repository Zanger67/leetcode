class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        output = 0
        helper = (lambda x: sum(map(int, x[:len(x) // 2])) == sum(map(int, x[len(x) // 2:])))
        while low <= high :
            if len(str(low)) % 2 == 1 :
                low = 10 ** ceil(log(low + 1, 10))
                continue
            if helper(str(low)) :
                output += 1
            low += 1
        return output
            