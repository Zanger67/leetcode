class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])

        # schema: {person:parent}
        #         {source parent:negative count of children} 
        uFind = {}
        latestTime = 0
        mostRecent = 0

        for log in logs :
            if log[1] not in uFind and log[2] not in uFind :
                uFind[log[2]] = -2
                uFind[log[1]] = log[2]
                latestTime = log[0]

            elif log[1] in uFind and log[2] in uFind :
                while uFind[log[1]] >= 0 :
                    log[1] = uFind[log[1]]
                while uFind[log[2]] >= 0 :
                    log[2] = uFind[log[2]]
                if log[1] == log[2] :
                    continue

                uFind[log[2]] += uFind[log[1]]
                uFind[log[1]] = log[2]
                latestTime = log[0]

            else :
                if log[1] in uFind :
                    log[1], log[2] = log[2], log[1]
                uFind[log[1]] = log[2]
                while uFind[log[2]] >= 0 :
                    log[2] = uFind[log[2]]
                uFind[log[2]] -= 1

            mostRecent = uFind[log[2]]
            latestTime = log[0]

        return latestTime if -mostRecent == n else -1