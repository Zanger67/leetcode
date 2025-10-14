class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # Indice setup O(s + max(a, b))
        a_indices = []
        b_indices = []
        a_i = 0
        while True :
            a_i = s.find(a, a_i)
            if a_i == -1 :
                break
            a_indices.append(a_i)
            a_i += 1
        b_i = 0
        while True :
            b_i = s.find(b, b_i)
            if b_i == -1 :
                break
            b_indices.append(b_i)
            b_i += 1
        
        # O(n log n) worst case
        output = []
        for i in a_indices :
            x = bisect.bisect(b_indices, i)
            if (x != 0 and abs(b_indices[x - 1] - i) <= k) or \
               (x != len(b_indices) and abs(b_indices[x] - i) <= k) :
                output.append(i)
        
        return output