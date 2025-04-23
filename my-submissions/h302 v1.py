class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def dfs(x: int, y: int, cords: List[int] = [x, y, x, y]) -> None :
            if not (0 <= x < len(image)) or not (0 <= y < len(image[0])) :
                return
            if image[x][y] == "0" :
                return

            if x < cords[0] :
                cords[0] = x
            elif x > cords[2] :
                cords[2] = x

            if y < cords[1] :
                cords[1] = y
            elif y > cords[3] :
                cords[3] = y

            image[x][y] = "0"
            dfs(x - 1, y, cords)
            dfs(x + 1, y, cords)
            dfs(x, y + 1, cords)
            dfs(x, y - 1, cords)
        
        output = [x, y, x, y]
        dfs(x, y, output)
        return (output[2] - output[0] + 1) * (output[3] - output[1] + 1)