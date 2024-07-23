class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        indx = 0
        counter = 0
        while indx < len(flowerbed) :
            if flowerbed[indx] :
                indx += 2
            elif indx and flowerbed[indx - 1] :
                indx += 1
            elif indx < len(flowerbed) - 1 and flowerbed[indx + 1] :
                indx += 3
            else :
                counter += 1
                indx += 2

            if counter >= n :
                return True

        return False