class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([(0, 0, 0)])
        offsets = [(-2, 1), (-2, -1), (-1, 2), (-1, -2),
                   (1, 2),  (1, -2),  (2, 1),  (2, -1)]
        visited = set()
        
        while q :
            x_curr, y_curr, cnt = q.popleft()
            if x == x_curr and y == y_curr :
                return cnt
            
            cnt += 1
            for dx, dy in offsets :
                x_new, y_new = x_curr + dx, y_curr + dy
                if (x_new, y_new) not in visited :
                    visited.add((x_new, y_new))
                    q.append((x_new, y_new, cnt))
        
        return -1