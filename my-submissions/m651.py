class Solution:
    def maxA(self, n: int) -> int:
        arr = [1, 2, 3, 4]
        arr_pair = [1] * 4

        while len(arr) < n :
            newVal = max(arr[len(arr) - 1] + arr_pair[len(arr) - 1],
                         3 * arr[len(arr) - 4])

            if newVal == 3 * arr[len(arr) - 4] :
                arr_pair.append(arr[len(arr) - 4])
            else :
                arr_pair.append(arr_pair[len(arr) - 1])

            arr.append(newVal)

        return arr[n - 1]