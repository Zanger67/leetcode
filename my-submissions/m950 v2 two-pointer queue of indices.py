class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        indices = deque(range(0, len(deck)))
        deck.sort()
        output = [0] * len(deck)

        deckSpot = 0
        while len(indices) > 1 :
            output[indices.popleft()] = deck[deckSpot]
            deckSpot += 1
            indices.append(indices.popleft())

        if indices :
            output[indices.pop()] = deck[deckSpot]
            
        return output
