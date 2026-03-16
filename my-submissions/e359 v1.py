class Logger:

    def __init__(self):
        self.messages = {}
        self.limitted = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.limitted and self.limitted[0][0] + 10 <= timestamp :
            t, m = self.limitted.popleft()
            if m in self.messages :
                self.messages.pop(m)

        if message in self.messages :
            return False
        
        self.limitted.append((timestamp, message))
        self.messages[message] = timestamp
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)