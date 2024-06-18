class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)

        output = [(-1 * freq, val) for val, freq in cnt.items()]
        heapq.heapify(output)

        actualOutput = []

        while output :
            freq, val = heapq.heappop(output)
            actualOutput.extend([val] * (freq * -1))
        
        return ''.join(actualOutput)