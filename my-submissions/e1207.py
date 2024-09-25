class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return len(cnt.values()) == len(set(cnt.values()))
