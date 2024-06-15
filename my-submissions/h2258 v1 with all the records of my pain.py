class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        toVisitPerson = deque([(1, 0, 1, inf, 1), (0, 1, 1, inf, 2)])  # (x, y, timeElapsed, maxWaitTime)
        toVisitFire = deque()               # (x, y)


        print()
        for gridRow in grid :
            print(''.join([f'{x}'.ljust(9) for x in gridRow]))
        print()


        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    grid[i][j] = (1, 0)             # (fire, timeSinceStart)
                    toVisitFire.append((i + 1, j, 1))
                    toVisitFire.append((i - 1, j, 1))
                    toVisitFire.append((i, j + 1, 1))
                    toVisitFire.append((i, j - 1, 1))


        while toVisitFire :
            fireX, fireY, time = toVisitFire.popleft()
            
            if not (0 <= fireX < len(grid)) or not (0 <= fireY < len(grid[0])) :
                continue
            
            # if (fireX == 0 == fireY) :
            #     continue

            # if ((fireX == len(grid) - 1) and (fireY == len(grid[0]) - 1))

            # Already fire so timine doesn't matter cause queue
            if isinstance(grid[fireX][fireY], tuple) :
                continue
            
            if grid[fireX][fireY] == 0 : # is grass
                grid[fireX][fireY] = (grid[fireX][fireY], time)

                time += 1
                toVisitFire.append((fireX + 1, fireY, time))
                toVisitFire.append((fireX - 1, fireY, time))
                toVisitFire.append((fireX, fireY + 1, time))
                toVisitFire.append((fireX, fireY - 1, time))
        
        print()
        for gridRow in grid :
            print(''.join([f'{x}'.ljust(9) for x in gridRow]))
        print()



        directionOfFireToSafehouse = -1     # 0 never set on fire, 1 above, 2 left, 3 both

        if isinstance(grid[len(grid) - 1][len(grid[0]) - 1], tuple) :
            above = grid[len(grid) - 2][len(grid[0]) - 1]
            left = grid[len(grid) - 1][len(grid[0]) - 2]

            if isinstance(above, tuple) and isinstance(left, tuple) :
                if above[1] == left[1] == grid[len(grid) - 1][len(grid[0]) - 1][1] - 1 == above[1] :
                    directionOfFireToSafehouse = 3
                elif above[1] == grid[len(grid) - 1][len(grid[0]) - 1][1] - 1 :
                    directionOfFireToSafehouse = 1
                else :
                    directionOfFireToSafehouse = 2
            elif isinstance(above, tuple) :
                directionOfFireToSafehouse = 1
            else :
                directionOfFireToSafehouse = 2
        else :
            directionOfFireToSafehouse = 0

            




        endReached = False
        infiniteTime = False
        masWaitTimeFound = -inf
        personVisited = {}           # (x, y) : maxWaitTimeFound
        while toVisitPerson :
            pX, pY, time, maxWaitTimeRn, directionVal = toVisitPerson.popleft()


            if not (0 <= pX < len(grid)) or not (0 <= pY < len(grid[0])) :
                continue

            if pX == 0 == pY :
                continue
            
            # wall
            if grid[pX][pY] == 2 :
                continue

            if (pX == len(grid) - 1) and (pY == len(grid[0]) - 1) :
                if not isinstance(grid[pX][pY], tuple) :
                    masWaitTimeFound = max(masWaitTimeFound, maxWaitTimeRn)
                    endReached = True
                    continue

                fireTime = grid[pX][pY][1]
                if fireTime < time :
                    continue
                timeDif = fireTime - time

                if timeDif < 0 : # NOTE: Potential issue here with < vs <= ?
                    continue
                maxWaitTimeRn = min(maxWaitTimeRn, timeDif)

                print('hihi')
                endReached = True



                # 0 never set on fire, 1 above, 2 left, 3 both
                if directionVal == directionOfFireToSafehouse :
                    maxWaitTimeRn += 1

                # print()
                # print(maxWaitTimeRn)
                # print(timeDif)
                # print('\t\t',masWaitTimeFound, maxWaitTimeRn)
                print('old max:\t', masWaitTimeFound)
                masWaitTimeFound = max(masWaitTimeFound, maxWaitTimeRn)
                print('new max:\t', masWaitTimeFound)
                # print(masWaitTimeFound)
                continue

            if (pX, pY) in personVisited :
                if personVisited[(pX, pY)] >= maxWaitTimeRn :
                    continue
            personVisited[(pX, pY)] = maxWaitTimeRn




            # NOTE: IF THIS IF STATEMENT IS TRIGGERED, IT'S EITHER
            # 1. END NOT REACHED AKA NO PATH
            # 2. INFEFINITE TIME ALLOWED

            # If fire can touch part of path, it can touch the whole path
            if not (pX == 0 == pY) and \
                not ((pX == len(grid) - 1) and (pY == len(grid[0]) - 1)) and \
                not isinstance(grid[pX][pY], tuple) :
                # print(grid[pX][pY])
                # print(not isinstance(grid[pX][pY], tuple))
                # return 10 ** 9
                # infiniteTime = True

                maxWaitTimeRn = inf
                time += 1
                toVisitPerson.append((pX + 1, pY, time, maxWaitTimeRn, 2))
                toVisitPerson.append((pX - 1, pY, time, maxWaitTimeRn, -1))
                toVisitPerson.append((pX, pY + 1, time, maxWaitTimeRn, 1))
                toVisitPerson.append((pX, pY - 1, time, maxWaitTimeRn, -1))

                continue
            
            # print(pX, pY)
            fireTime = grid[pX][pY][1]

            # timeDif > 0  --> we made it
            # timeDif <= 0 --> we burned
            timeDif = fireTime - time


            # Less than or equal cause means if the fire catches 
            # up to the square you're on
            # The only exception to this rule is if it's the final 
            # safehouse square
            if timeDif <= 0 : # NOTE: Potential issue here with < vs <= ?
                continue

            # print(pX, pY)
            # print(timeDif)
            # print(fireTime, time)
            # print()

            # print(timeDif)
            maxWaitTimeRn = min(maxWaitTimeRn, timeDif)
            time += 1

            toVisitPerson.append((pX + 1, pY, time, maxWaitTimeRn, 2))
            toVisitPerson.append((pX - 1, pY, time, maxWaitTimeRn, -1))
            toVisitPerson.append((pX, pY + 1, time, maxWaitTimeRn, 1))
            toVisitPerson.append((pX, pY - 1, time, maxWaitTimeRn, -1))
        
        if not endReached :
            return -1

        # if infiniteTime :
        #     return 10 ** 9

        return 10 ** 9 if masWaitTimeFound == inf \
                        else max(masWaitTimeFound - 1, 0) if masWaitTimeFound != -inf \
                        else -1