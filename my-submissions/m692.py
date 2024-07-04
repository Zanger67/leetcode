class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = list(Counter(words).items())
        counter.sort()
        counter.sort(key=lambda x: x[1], reverse=True)
        
        return [counter[x][0] for x in range(k)]
