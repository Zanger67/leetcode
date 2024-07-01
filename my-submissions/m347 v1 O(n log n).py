# Prompt follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        cnt = Counter(nums)

        # O(n log n)
        keys = sorted(cnt.keys(), reverse=True, key=lambda x: cnt.get(x))

        return keys[0:min(k, len(keys))]