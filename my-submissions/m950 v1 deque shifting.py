class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        print(deck)

        output = deque()

        for card in deck :
            if len(output) > 0 :
                output.appendleft(output.pop())
            
            output.appendleft(card)
        return list(output)

