''' notes
    output[i] = x where x ^ output[i-1] == pref[i]
'''

# removal of the append increases runtime dramatically --> pre-defined arr len instead
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        runningXOR = pref[0]
        for i in range(1, len(pref)) :
            # I swapped to using the same array to save memory which significantly lowered the cost making this consistently 90+%
            pref[i] = runningXOR ^ pref[i] 
            runningXOR ^= pref[i]

        return pref



# class Solution:
#     def findArray(self, pref: List[int]) -> List[int]:
#         output = [pref[0]]
#         runningXOR = pref[0]

#         # print(5 ^ 2) # finding pref[1] --> 7
#         # print(5 ^ 7 ^ 0) # finding pref[0] --> 2

#         for i in range(1, len(pref)) :
#             output.append(runningXOR ^ pref[i])
#             runningXOR ^= (runningXOR ^ pref[i])

#         return output