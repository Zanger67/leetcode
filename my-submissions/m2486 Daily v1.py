# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/?envType=daily-question&envId=2024-06-03


# 5% for both memory and runtime sob


# I'm realizing in hindsight that a dictionary wasn't necessary since I could just
# Iterate through using two pointers and it would still be O(m + n)

# This is what I get for doing it the moment I wake up at 630am sob

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if s == t:
            return 0

        # Getting the indicies of each value and storing them for O(1) lookups
        sSpots = {}
        for i in range(len(s)) :
            temp = sSpots.get(s[i], [])
            temp.append(i)
            sSpots[s[i]] = temp
        

        currentSpotT: int = 0
        currentSpotS = -1
    
        # Go until we can't find a index to use that's farther than our current spot
        while currentSpotT < len(t) :
            temp = sSpots.get(t[currentSpotT], [])

            if len(temp) == 0 :
                break

            while True :
                indCheck = temp.pop(0)
                if indCheck > currentSpotS :
                    currentSpotS = indCheck
                    sSpots[t[currentSpotT]] = temp
                    break

                if len(temp) == 0 :
                    return len(t) - currentSpotT
            currentSpotT += 1

        return len(t) - currentSpotT
