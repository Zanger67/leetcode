class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = Counter([num % value for num in nums])
        output, output_modded = 0, 0

        while output_modded in mods :
            mods[output_modded] -= 1
            if mods[output_modded] == 0 :
                mods.pop(output_modded)
            output += 1
            output_modded = (output_modded + 1) % value

        return output