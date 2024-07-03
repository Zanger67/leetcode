# NOTE: Literally on the edge of runtimes lol
# Passes runtime ~50% of the time, other half it barely fails

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        minn, maxx = sick[0], sick[-1]

        totalToInfect = 0
        groupSizes = [(0, 0)]
        output = 1

        if minn > 0 :
            totalToInfect += minn
            groupSizes.append((minn, minn))
        if n - maxx - 1 > 0 :
            count = n - maxx - 1
            totalToInfect += count
            groupSizes.append((count, count + groupSizes[-1][1]))

        for i in range(1, len(sick)) :
            numPeople = sick[i] - sick[i - 1] - 1
            if numPeople > 0 :
                totalToInfect += numPeople
                groupSizes.append((numPeople, numPeople + groupSizes[-1][1]))
                output *= 2 ** (numPeople - 1)

        def multinomial(groups: List[Tuple[int, int]]):
            modd = 10 ** 9 + 7
            return math.prod(math.comb(x[1], x[0]) % (modd) for x in groups)

        return (output * multinomial(groupSizes[1:])) % (10 ** 9 + 7)


