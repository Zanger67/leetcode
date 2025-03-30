class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = t = output = 0

        while t < len(target) :
            loop = len(source)

            while loop >= 0 and source[s] != target[t] :
                s += 1
                loop -= 1
                if s >= len(source) :
                    output += 1
                    s -= len(source)

            if source[s] != target[t] :
                return -1

            s += 1
            t += 1
            if s >= len(source) :
                output += 1
                s -= len(source)

        if s > 0 :
            output += 1

        return output