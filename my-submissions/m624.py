class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1, min2 = inf, inf
        min1indx, min2indx = -1, -1

        max1, max2 = -inf, -inf
        max1indx, max2indx = -1, -1

        for i, arr in enumerate(arrays) :
            if arr[0] < min1 :
                min1, min2 = arr[0], min1
                min1indx, min2indx = i, min1indx
            elif arr[0] < min2 :
                min2 = arr[0]
                min2indx = i

            if arr[-1] > max1 :
                max1, max2 = arr[-1], max1
                max1indx, max2indx = i, max1indx
            elif arr[-1] > max2 :
                max2 = arr[-1]
                max2indx = i


        # A bit less efficient since I use a list pointer but
        # it simplifies the code a lot and it's a constant cost 
        # since it'll either be the value immediately or it'll be 
        # 1 of 3 possible combinations.
        if min1indx != max1indx :
            return max1 - min1

        outputs = []
        if min1indx != max2indx :
            outputs.append(max2 - min1)
        if min2indx != max1indx :
            outputs.append(max1 - min2)
        if min2indx != max2indx :
            outputs.append(max2 - min2)

        return max(outputs)
        