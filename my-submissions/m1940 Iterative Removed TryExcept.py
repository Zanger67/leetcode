# https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/description/?envType=weekly-question&envId=2024-06-01
# weekly premium question

''' Notes
    I adjusted this from the original first success attempt to avoid the try-except block since
    I thought maybe that could cause overhead and while it did "improve," it's changed from a 
    consistently above-average runtime (bad) to a inconsistently high-low ranging runtime. On average,
    it *is* better... the first run I tried with it resulted in a top 95% lol. But idk. It's interesting.
'''


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        output = []

        pointers = [0] * len(arrays)
        maxCurrent = arrays[0][pointers[0]]
        pointerOfPointer = 1

        counter = 1
        while pointers[pointerOfPointer] < len(arrays[pointerOfPointer]) :
            if arrays[pointerOfPointer][pointers[pointerOfPointer]] < maxCurrent :
                pointers[pointerOfPointer] += 1
                continue

            if arrays[pointerOfPointer][pointers[pointerOfPointer]] > maxCurrent :
                maxCurrent = arrays[pointerOfPointer][pointers[pointerOfPointer]]
                counter = 1
                pointerOfPointer = (pointerOfPointer + 1) % len(pointers)
                continue
            
            counter += 1
            pointers[pointerOfPointer] += 1
            pointerOfPointer = (pointerOfPointer + 1) % len(pointers)
            
            if counter == len(pointers) :
                output.append(maxCurrent)
                counter = 0

        return output

