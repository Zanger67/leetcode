
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        upward_prefix_sum = [0]     # prefix sum of POSITIVE DIFFERENCES
        hp = []                     # (distance_upwards, index) MAXHEAP

        for indx, (i, j) in enumerate(zip(heights[:-1], heights[1:]), 1) :
            upwards = max(j - i, 0)
            upward_prefix_sum.append(upward_prefix_sum[-1] + upwards)

            # Ladder and bricks will only be used if it's an upwards movement
            if upwards :
                heapq.heappush(hp, (-upwards, indx))        # negative cause max heap

        curr_ladder_savings = 0
        ladder_spots = []           # max Heap[Tuple[index, distance_upwards]]
                                    # The building gaps that we'll use ladders for

        while ladders > 0 and hp :
            dist_up, indx = heapq.heappop(hp)
            dist_up *= -1
            ladders -= 1

            heapq.heappush(ladder_spots, (-indx, dist_up))  # negative cause max heap - indxs should be unique
            curr_ladder_savings += dist_up


        # If we havev to scrap a ladder plan due to not enough bricks, then we
        # can't really choose a *farther* spot so this helps us avoid unncessary
        # operations
        max_ladder_indx = inf
        last_ladder_indx = 0

        if ladder_spots :
            while bricks < upward_prefix_sum[-ladder_spots[0][0]] - curr_ladder_savings :
                # Remove the FARTHEST INDEX ladder usage since we can't go 
                # farther than there
                indx, dist_up = heapq.heappop(ladder_spots)
                indx *= -1
                curr_ladder_savings -= dist_up

                # Remove anything beyond that point since we already know we can't
                # go farther
                max_ladder_indx = min(max_ladder_indx, indx)
                while hp and hp[0][1] >= max_ladder_indx :
                    heapq.heappop(hp)

                # Add newly selected ladder spot
                dist_up, indx = heapq.heappop(hp)
                dist_up *= -1

                curr_ladder_savings += dist_up
                heapq.heappush(ladder_spots, (-indx, dist_up))

            last_ladder_indx = -ladder_spots[0][0]

        # Use remaining bricks
        for i in range(last_ladder_indx, len(upward_prefix_sum)) :
            if upward_prefix_sum[i] - curr_ladder_savings > bricks :
                return i - 1

        return len(upward_prefix_sum) - 1
