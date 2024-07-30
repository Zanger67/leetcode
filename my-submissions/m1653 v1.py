class Solution:
    def minimumDeletions(self, s: str) -> int:
        s = deque(s)
        counter = 0

        cnt = Counter(s)

        while s :
            if s[0] == 'a' :
                s.popleft()
                cnt['a'] -= 1
                continue
            if s[-1] == 'b' :
                s.pop()
                cnt['b'] -= 1
                continue

            # which is blocking the least
            counter += 1
            if cnt['a'] > cnt['b'] :
                cnt['b'] -= 1
                s.popleft()
            else :
                cnt['a'] -= 1
                s.pop()

        return counter