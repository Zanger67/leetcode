class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Since inputs aren't sorted by time period order
        # NOTE: x[1] not needed since input is guarenteed not
        # to contain overlapping times within the same slot list
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        indx1, indx2 = 0, 0
        while indx1 < len(slots1) and indx2 < len(slots2) :
            s1, e1, s2, e2 = slots1[indx1] + slots2[indx2]

            # Calculate middle gap
            if min(e1, e2) - max(s1, s2) >= duration :
                return [max(s1, s2), max(s1, s2) + duration]

            # Keep the period that ends later
            if e1 < e2 :
                indx1 += 1
            else :
                indx2 += 1

        # None found
        return []
