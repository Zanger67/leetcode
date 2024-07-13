# By far not optimized but I wanted to see if it would pass and 
# I was aiming for speed. Managed to get an AC with this code in 14m:48s :)

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # (position, direction, health, origIndx)
        posDir = sorted([(pd[0], pd[1], pd[2], origIndx) for origIndx, pd in enumerate(zip(positions, directions, healths))], key=lambda x: x[0])

        popped = []
        escaped = []
        while posDir :
            if posDir[-1][1] == 'L' :
                popped.append(posDir.pop())
            elif not popped : # R and no L to the right
                escaped.append(posDir.pop())
            else :
                if posDir[-1][2] > popped[-1][2] :
                    popped.pop()
                    posDir[-1] = (posDir[-1][0], posDir[-1][1], posDir[-1][2] - 1, posDir[-1][3])
                elif posDir[-1][2] < popped[-1][2] :
                    posDir.pop()
                    popped[-1] = (popped[-1][0], popped[-1][1], popped[-1][2] - 1, popped[-1][3])
                else :
                    popped.pop()
                    posDir.pop()

        return [x[2] for x in sorted(popped + escaped, key=lambda x: x[3])]