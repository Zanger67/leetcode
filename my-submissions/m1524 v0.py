class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        for i in range(1, len(arr)) :
            arr[i] += arr[i - 1]

        arr[0] = (arr[0] % 2, (arr[0] + 1) % 2)     # (# odds, # evens)
        for i in range(1, len(arr)) :
            arr[i] = (arr[i - 1][0] + arr[i] % 2, arr[i - 1][1] + (arr[i] + 1) % 2)

        return arr[-1][0] + arr[-1][1] * arr[-1][0] % (10 ** 9 + 7)