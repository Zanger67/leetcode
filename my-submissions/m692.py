# https://leetcode.com/problems/top-k-frequent-words/description/

# Sorting and heapifying are both nlogn so i thought it would be simpler
# this way since it uses native functions vs us iterating
# and flipping priorities to negative to create a max heap via
# the 2nd value in each tuple or having to manually add them

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = list(Counter(words).items())
        counter.sort()
        counter.sort(key=lambda x: x[1], reverse=True)
        
        return [counter[x][0] for x in range(k)]
