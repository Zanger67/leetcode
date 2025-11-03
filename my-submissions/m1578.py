class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        output = 0
        curr = 0

        while curr < len(colors) :
            tot = neededTime[curr]
            color, maxx = colors[curr], neededTime[curr]

            for i in range(curr + 1, len(colors)) :
                if colors[i] != color :
                    break
                curr = i
                maxx = max(maxx, neededTime[i])
                tot += neededTime[i]

            output += tot - maxx
            curr += 1

        return output