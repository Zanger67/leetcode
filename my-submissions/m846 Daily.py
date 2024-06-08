# https://leetcode.com/problems/hand-of-straights/description/?envType=daily-question&envId=2024-06-06

# I suspect it may be easier/more efficient if I use a counter / dict and match keys but this does
# consistently work at 80%+ on both runtime and space

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize :
            return False
        if groupSize == 1 :
            return True

        heapq.heapify(hand)

        for groups in range(len(hand) // groupSize) :
            current = heapq.heappop(hand)
            readdLater = []

            cnt = 0
            while cnt < groupSize - 1 :
                if (len(hand) == 0) :
                    return False

                temp = heapq.heappop(hand)
                if not (temp - current) :
                    readdLater.append(temp)
                    continue
                elif not (temp - current == 1) :
                    print('hi')
                    return False
                current = temp
                cnt += 1
            
            for x in readdLater :
                heapq.heappush(hand, x)

        return True