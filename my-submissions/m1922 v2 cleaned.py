class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def _helper(tot_cases: int, poww: int, mod_val: int = 10 ** 9 + 7) :
            if tot_cases == 0 :
                return 1
            output, x = poww, 1
            prev = []
            while 2 * x <= tot_cases :
                prev.append((x, output))
                output = (output * output) % mod_val
                x *= 2
            while prev :
                i, poww = prev.pop()
                if x + i <= tot_cases :
                    x += i
                    output = (output * poww) % mod_val
            return output

        mod_val = 10 ** 9 + 7
        return (
            _helper((n // 2) + (n % 2), 5, mod_val) * 
            _helper((n // 2), 4, mod_val)
        ) % (mod_val)