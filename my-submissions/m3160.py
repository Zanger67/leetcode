class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls         = {}
        colour_counts = {}
        output        = []

        for ball, colour in queries :
            if ball not in balls :
                balls[ball] = colour
                colour_counts[colour] = colour_counts.get(colour, 0) + 1
                output.append(len(colour_counts))
                continue

            if colour == balls[ball] :
                output.append(len(colour_counts))
                continue

            if colour_counts[balls[ball]] == 1 :
                colour_counts.pop(balls[ball])
            else :
                colour_counts[balls[ball]] -= 1

            balls[ball] = colour
            colour_counts[colour] = colour_counts.get(colour, 0) + 1
            output.append(len(colour_counts))

        return output