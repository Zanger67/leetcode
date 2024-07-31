class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def recurs(currBook: int = 0,
                    height: int = 0, 
                    widthRemaining: int = 0) -> int :
            if currBook >= len(books) :
                return 0
            
            # New row
            output = books[currBook][1] + recurs(currBook + 1,
                                                 books[currBook][1],
                                                 shelfWidth - books[currBook][0])

            # Can current book can fit in current row
            if widthRemaining - books[currBook][0] >= 0 :
                heightIncr = max(0, books[currBook][1] - height)
                output = min(output, 
                             heightIncr + recurs(currBook + 1, 
                                                 height + heightIncr,  
                                                 widthRemaining - books[currBook][0]))

            return output
        
        if not books :
            return 0
        return recurs()