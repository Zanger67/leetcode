''' Notes
    In essence, we have x positions and m balls, and we need to find AN ideal
    way where we can place the m balls into m positions so that the min distance
    between the balls is minimized

    The ideal case will be (max(position) - min(position)) / (m - 1)
'''

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        minn = maxx = position[0]

        for p in position :
            if p < minn :
                minn = p
            elif p > maxx :
                maxx = p

        left = 1                            # 1 = worst case since m=len(positions) += 1 each indx worst
        right = (maxx - minn) // (m - 1)    # m - 1 = number of gaps so this is aideal case 

        while left < right :
            mid = (left + right + 1) // 2
            worked = False
            counter = 1
            prevVal = position[0]

            for i in range(1, len(position)) :
                if position[i] - prevVal >= mid :
                    counter += 1
                    prevVal = position[i]

                    if counter >= m :
                        worked = True
                        break

            if worked :
                left = mid
            else : 
                right = mid - 1

        return left