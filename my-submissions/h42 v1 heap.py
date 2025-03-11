class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0

        vals = [(-x, i) for i, x in enumerate(height)]
        heapify(vals)

        left_max = right_max = heappop(vals)[1]
        while vals and (left_max > 0 or right_max < len(height) - 1):
            val, i = heappop(vals)
            val = -val

            if left_max <= i <= right_max :
                continue

            if i <= left_max :
                minn = min(val, height[left_max])
                output += sum(minn - x for x in height[i + 1:left_max])
                left_max = i
            else :
                minn = min(val, height[right_max])
                output += sum(minn - x for x in height[right_max + 1:i])
                right_max = i
                
        return output