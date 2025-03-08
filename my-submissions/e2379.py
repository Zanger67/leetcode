class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        output = w = blocks[:k].count('W')
        for l, r in zip(blocks, blocks[k:]) :
            w += (r == 'W') - (l == 'W')
            output = min(output, w)
        return output