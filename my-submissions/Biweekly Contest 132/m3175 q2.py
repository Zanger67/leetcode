# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:        
        gaming = deque(list(range(0,len(skills))))
        wins = {}

        currentKingOfHill = gaming.popleft()
        counter = 0
        while wins.get(currentKingOfHill, 0) < k :
            if counter > len(skills) :
                return currentKingOfHill
            if skills[currentKingOfHill] > skills[gaming[0]] :
                gaming.append(gaming.popleft())
                counter += 1
            else :
                counter = 0
                gaming.append(currentKingOfHill)
                currentKingOfHill = gaming.popleft()
            wins[currentKingOfHill] = wins.get(currentKingOfHill, 0) + 1
        return currentKingOfHill