class FileSystem:

    def __init__(self):
        self.trie = {}

    def createPath(self, path: str, value: int) -> bool:
        pathChunks = path.split('/')[1:]

        curr = self.trie
        for i in range(len(pathChunks) - 1) :
            if pathChunks[i] not in curr :
                return False
            curr = curr[pathChunks[i]]

        if pathChunks[-1] in curr and 'value' in curr[pathChunks[-1]] :
            return False

        curr[pathChunks[-1]] = {}
        curr[pathChunks[-1]]['value'] = value
        return True

    def get(self, path: str) -> int:
        pathChunks = path.split('/')[1:]

        curr = self.trie
        for chunk in pathChunks :
            if chunk not in curr :
                return -1
            curr = curr[chunk]
        
        if 'value' in curr :
            return curr['value']
        return -1
        



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)