# https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/description/?envType=weekly-question&envId=2024-06-01
# weekly premium question

# Rank: 3

# Method iterates through O(m*n) where m=len(arrays) and n=max(len(array[i]))


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        output = []

        pointers = [0] * len(arrays)
        maxCurrent = arrays[0][pointers[0]]
        pointerOfPointer = 1

        counter = 1
        try :
            while True :
                if arrays[pointerOfPointer][pointers[pointerOfPointer]] < maxCurrent :
                    pointers[pointerOfPointer] += 1
                    continue

                if arrays[pointerOfPointer][pointers[pointerOfPointer]] > maxCurrent :
                    maxCurrent = arrays[pointerOfPointer][pointers[pointerOfPointer]]
                    counter = 1
                    pointerOfPointer = (pointerOfPointer + 1) % len(pointers)
                    continue

                if counter == len(pointers) :
                    output.append(maxCurrent)
                    pointers = [i + 1 for i in pointers]
                    counter = 0
                    continue
                
                counter += 1
                pointerOfPointer = (pointerOfPointer + 1) % len(pointers)
        except IndexError :
            return output

