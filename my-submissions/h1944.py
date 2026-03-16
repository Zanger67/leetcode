class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        output = [0] * len(heights)
        stk = []

        for i, h in enumerate(reversed(heights)) :
            while stk and stk[-1] <= h :
                stk.pop()
                output[i] += 1
            if stk :
                output[i] += 1
            stk.append(h)

        return output[::-1]