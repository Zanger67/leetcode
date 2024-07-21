
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        # only positives are passed into here
        def zeroHelper(nums: List[int], offset: int = 0) -> int :
            if not nums :
                return 0
            if len(nums) == 1 :
                return nums[0] + offset

            valDif = -1 * min(nums)
            counter = (-valDif + offset)

            prev = 0
            prevIsZero = True
            for i, val in enumerate(nums) :
                val += valDif
                if val == 0 :
                    if not prevIsZero :
                        counter += zeroHelper(nums[prev:i], valDif)
                    prev = i + 1
                    prevIsZero = True
                else :
                    prevIsZero = False

            counter += zeroHelper(nums[prev:], valDif)
            return counter

        difs = [nums[x] - target[x] for x in range(len(nums))]
        counter = 0

        prev = 0
        prevPositive = True
        prevIsZero = True
        for i, val in enumerate(difs) :
            currIsPos = bool(val > 0)
            if val == 0 :
                if not prevIsZero :
                    counter += zeroHelper([abs(x) for x in difs[prev:i]])
                prev = i + 1
                prevIsZero = True
            elif currIsPos != prevPositive and not prevIsZero:
                counter += zeroHelper([abs(x) for x in difs[prev:i]])
                prev = i
            else :
                prevIsZero = False

            prevPositive = currIsPos
        counter += zeroHelper([abs(x) for x in difs[prev:]])

        return counter