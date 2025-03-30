class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = output = 0

        for t in target :
            for _ in repeat(None, len(source)) :
                if source[s] == t :
                    break
                s = (s + 1) % len(source)
                output += 1

            if source[s] != t :
                return -1
            output += 1
            s = (s + 1) % len(source)

        return ceil(output / len(source))