class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.spot = 0

    def visit(self, url: str) -> None:
        self.spot += 1
        if self.spot < len(self.history) :
            self.history = self.history[:self.spot]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.spot = max(0, self.spot - steps)
        return self.history[self.spot]

    def forward(self, steps: int) -> str:
        self.spot = min(len(self.history) - 1, self.spot + steps)
        return self.history[self.spot]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)