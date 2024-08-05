class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = set()
        notdistinct = set()

        for s in arr :
            if s in notdistinct :
                continue
            if s in distinct :
                distinct.remove(s)
                notdistinct.add(s)
            else :
                distinct.add(s)

        
        if k > len(distinct) :
            return ""
        
        for x in arr :
            if x not in distinct :
                continue
            k -= 1

            if k <= 0 :
                return x
        
        return 'error'
