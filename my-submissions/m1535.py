# Did this one cause apparently it was very close tot he BW 132 contest q2 and it was lol
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = {}
        playerQueue = deque(arr)

        king = playerQueue.popleft()
        counter = 0
        while wins.get(king, 0) < k :
            if counter == len(arr) :
                break
            counter += 1

            if king > playerQueue[0] :
                wins[king] = wins.get(king, 0) + 1
                playerQueue.append(playerQueue.popleft())
            else :
                playerQueue.append(king)
                king = playerQueue.popleft()
                wins[king] = 1
        return king