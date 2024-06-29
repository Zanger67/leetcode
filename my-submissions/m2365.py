class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        lastOccurance = {}

        for i in range(len(tasks)) :
            if tasks[i] in lastOccurance and day - lastOccurance[tasks[i]] < space :
                day = lastOccurance[tasks[i]] + space
            day += 1
            lastOccurance[tasks[i]] = day

        return day