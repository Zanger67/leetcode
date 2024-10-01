class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if k == 1 :
            return True

        # Count the remainders after mods
        remainders = [0] * k
        for num in arr :
            remainders[num % k] += 1

        return all(remainders[x] == remainders[k - x] for x in range(1, k // 2)) and \
                ((k % 2 == 1 and remainders[k // 2] == remainders[ceil(k / 2)]) or 
                 (k % 2 == 0 and remainders[k // 2] % 2 == 0))
