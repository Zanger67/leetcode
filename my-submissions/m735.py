class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        stk = []

        while asteroids :
            # going right
            if asteroids[-1] > 0 :
                # while current asteroid is larger than the ones going left
                while stk and stk[-1] + asteroids[-1] > 0 :
                    stk.pop()
                
                # if same size
                if stk and stk[-1] == -asteroids[-1] :
                    asteroids.pop()
                    stk.pop()
                # no astroids not destroyed going left
                elif not stk :
                    output.append(asteroids.pop())
                # asteroid going left is larger than current
                else : # smaller
                    asteroids.pop()
            # asteroid going left
            else :
                stk.append(asteroids.pop())

        return stk[::-1] + output[::-1]