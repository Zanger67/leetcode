class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        trie = {}

        for num in nums :
            curr = trie
            for c in num :
                curr[-1] = curr.get(-1, 0) + 1      # Count cases
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
        
        output = []

        while len(output) < len(nums[0]) :
            if not trie :
                output.append('0')
            elif len(trie) == 3 :
                zero = trie['0'].get(-1, 0)
                one = trie['1'].get(-1, 0)

                if zero > one :
                    output.append('0')
                    trie = trie.get('0')
                else :
                    output.append('1')
                    trie = trie.get('1')
            elif '0' in trie :
                output.append('1')
                trie = None
            else :
                output.append('0')
                trie = None
                

        return ''.join(output)