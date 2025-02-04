class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        N, S, E, W = 0, 0, 0, 0
        output_max = 0

        for c in s :
            match c :
                case 'N' :
                    N += 1
                case 'S' :
                    S += 1
                case 'E' :
                    E += 1
                case 'W' :
                    W += 1
                case _ :
                    pass

            output_max = max(output_max, abs(N - S) + abs(E - W) + 2 * (min(k, min(N, S) + min(E, W))))

        return output_max