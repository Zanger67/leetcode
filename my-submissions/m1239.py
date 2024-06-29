class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arrTuples = []

        for s in arr :
            stringSet = set(s)
            if len(s) == len(stringSet) :
                arrTuples.append(stringSet)


        self.maxx = 0
        def helper(current: set(), toTry: List[Set[str]]) -> None :
            self.maxx = max(self.maxx, len(current))
            if not toTry :
                return
            
            nextToTry = toTry.pop()
            helper(current, toTry)
            temp = nextToTry | current
            if len(current) + len(nextToTry) == len(temp) :
                helper(temp, toTry)
            toTry.append(nextToTry)

        helper(set(), arrTuples)
        return self.maxx