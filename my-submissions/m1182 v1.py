class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        indices = {1: [], 2: [], 3:[]}
        for i, c in enumerate(colors) :
            indices[c].append(i)

        return [
            0 if colors[i] == c else self._bin_search_closest(indices[c], i)
            for i, c in queries
        ]

    def _bin_search_closest(self, arr: List[int], target_indx: int) -> int :
        if not arr :
            return -1
        l, r = 0, len(arr) - 1

        while l < r :
            mid = (l + r) // 2
            mid_val = arr[mid]
            if mid_val == target_indx :
                return 0
            if mid_val > target_indx :
                r = mid - 1
                continue
            l = mid + 1

        # Fuzzy bound so check +/- 1 index to see if it's an approximation
        return min(abs(target_indx - x) for x in arr[max(0, l - 1):min(len(arr), r + 2)])