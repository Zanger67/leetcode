class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        output = 0
        prev = 0
        for r in bank :
            laz = r.count('1')
            if laz == 0 :
                continue
            output += laz * prev
            prev = laz
        return output