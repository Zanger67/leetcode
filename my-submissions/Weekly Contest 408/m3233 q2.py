class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        primes = [2, 3, 5]
        offset = 2
        while primes[-1] ** 2 <= r :
            nextPrime = primes[-1] + offset
            isPrime = True
            for prime in primes :
                if prime ** 2 > nextPrime :
                    break
                if nextPrime % prime == 0 :
                    isPrime = False
                    break

            if isPrime :
                offset = 2
                primes.append(nextPrime)
            else :
                offset += 2

        starterIndx = bisect_left(primes, ceil(sqrt(l)))

        while primes and primes[-1] ** 2 > r :
            primes.pop()

        return r - l + 1 - (len(primes) - starterIndx)