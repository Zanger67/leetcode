class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        left, right = list(reversed(s)), []

        while left :
            curr = left.pop()
            right.append(curr)
            if len(left) >= len(part) - 1 and curr == part[0] :
                matches = True
                for i in range(len(part) - 1) :
                    right.append(left.pop())
                    if right[-1] != part[i + 1] :
                        matches = False
                        for j in range(i + 1) :
                            left.append(right.pop())
                        break
                    
                if matches :
                    for i in range(len(part)) :
                        right.pop()
                    for i in range(min(len(part), len(right))) :
                        left.append(right.pop())

        return ''.join(right)