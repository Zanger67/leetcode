class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = output = 0 
        left, right = 0, len(height) - 1

        while left < right :
            if height[left] < height[right] :
                output += (left_max := max(left_max, height[left])) - height[left]
                left += 1
            else :
                output += (right_max := max(right_max, height[right])) - height[right]
                right -= 1

        return output