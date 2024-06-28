class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        folder.sort()
        output = []


        for f in folder :
            path = f.split('/')[1:]
            curr = trie
            add = False
            for c in path :
                if c not in curr :
                    curr[c] = {}
                    add = True
                if False in curr :
                    break

                curr = curr[c]

            if add and False not in curr:
                output.append(f)
                curr[False] = True

        return output