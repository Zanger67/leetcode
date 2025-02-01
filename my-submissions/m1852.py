class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        output = []
        arr = deque([-1] + nums[:k - 1])
        cnt = Counter(arr)
        for val in nums[k - 1:] :
            rem = arr.popleft()
            if cnt[rem] == 1 :
                cnt.pop(rem)
            else :
                cnt[rem] -= 1

            arr.append(val)
            cnt[val] += 1
            output.append(len(cnt))

        return output
