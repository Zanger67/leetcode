class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        pilesDq = deque(piles)
        alice, bob = 0, 0
        who = True
        while pilesDq :
            maxx = 0
            if pilesDq[0] > pilesDq[-1] :
                maxx = pilesDq.popleft()
            else :
                maxx = pilesDq.pop()

            if who :
                alice += maxx
            else :
                bob += maxx

        return alice > bob
