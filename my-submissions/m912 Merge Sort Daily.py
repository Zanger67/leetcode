class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums: List[int]) -> List[int] :
            if len(nums) <= 1 :
                return nums
            
            left = mergeSort(nums[:len(nums) // 2])
            right = mergeSort(nums[len(nums) // 2:])
            leftIndx = 0
            rightIndx = 0

            output = []

            while leftIndx < len(left) and rightIndx < len(right) :
                if left[leftIndx] < right[rightIndx] :
                    output.append(left[leftIndx])
                    leftIndx += 1
                else :
                    output.append(right[rightIndx])
                    rightIndx += 1

            output.extend(left[leftIndx:])
            output.extend(right[rightIndx:])

            return output
        return mergeSort(nums)