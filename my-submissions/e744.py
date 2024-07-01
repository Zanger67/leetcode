class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left < right :
            mid = (left + right) // 2
            
            if ord(letters[mid]) <= ord(target) :
                left = mid + 1
                continue

            right = mid - 1
        
        if (ord(letters[left]) <= ord(target)) :
            return letters[(left + 1) % len(letters)]
        return letters[left]