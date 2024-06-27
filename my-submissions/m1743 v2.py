class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mappings = defaultdict(list)
        starters = set()

        # Mapping
        for pair in adjacentPairs :
            mappings[pair[0]].append(pair[1])
            mappings[pair[1]].append(pair[0])
            
        # Find starter
        starter = -1
        for k, v in mappings.items() :
            if len(v) == 1 :
                starter = k
                break
        

            
        output = [starter]
        while len(output) <= len(adjacentPairs) :
            options = mappings[output[-1]]

            if len(options) <= 1 :
                output.append(options[0])
            elif output[-2] != options[0] :
                output.append(options[0])
            else :
                output.append(options[1])

        return output