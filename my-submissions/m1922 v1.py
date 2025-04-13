class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod_val = 10 ** 9 + 7
        # evens
        evens = 1
        tot_cases = (n // 2) + (n % 2)
        prev = []
        if tot_cases > 0 :
            evens = 5
            x = 1
            while 2 * x <= tot_cases :
                prev.append((x, evens))
                evens = (evens * evens) % mod_val
                x *= 2
            while prev :
                i, pow5 = prev.pop()
                if x + i <= tot_cases :
                    x += i
                    evens *= pow5
        
        # odds
        odds = 1
        tot_cases = (n // 2)
        prev = []
        if tot_cases > 0 :
            odds = 4
            x = 1
            while 2 * x <= tot_cases :
                prev.append((x, odds))
                odds = (odds * odds) % mod_val
                x *= 2
            while prev :
                i, pow4 = prev.pop()
                if x + i <= tot_cases :
                    x += i
                    odds *= pow4


        return (evens * odds) % (mod_val)