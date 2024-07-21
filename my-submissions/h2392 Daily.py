class Solution:
    def buildMatrix(self, 
                    k: int, 
                    rowConditions: List[List[int]], 
                    colConditions: List[List[int]]) -> List[List[int]]:

        # rows
        paths = [[] for _ in range(k + 1)]
        deg = [0] * (k + 1)
        pathRows = []

        for x, y in rowConditions :
            paths[x].append(y)
            deg[y] += 1
        
        dequeueueueueueue = deque()
        for i, d in enumerate(deg[1:], 1) :
            if not d :
                dequeueueueueueue.append(i)
        counter = 0
        while dequeueueueueueue :
            curr = dequeueueueueueue.popleft()
            pathRows.append(curr)
            counter += 1

            for nxt in paths[curr] :
                deg[nxt] -= 1
                if not deg[nxt] :
                    dequeueueueueueue.append(nxt)

        if counter != k :
            return []



        # cols
        paths = [[] for _ in range(k + 1)]
        deg = [0] * (k + 1)
        pathCols = []

        for x, y in colConditions :
            paths[x].append(y)
            deg[y] += 1
        
        dequeueueueueueue = deque()
        for i, d in enumerate(deg[1:], 1) :
            if not d :
                dequeueueueueueue.append(i)
        counter = 0
        while dequeueueueueueue :
            curr = dequeueueueueueue.popleft()
            pathCols.append(curr)
            counter += 1

            for nxt in paths[curr] :
                deg[nxt] -= 1
                if not deg[nxt] :
                    dequeueueueueueue.append(nxt)

        if counter != k :
            return []


        output = [[0] * k for _ in range(k)]
        for i in range(k) :
            for j in range(k) :
                if pathRows[i] == pathCols[j] :
                    output[i][j] = pathRows[i]
        return output

