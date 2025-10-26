class Bank:

    def __init__(self, balance: List[int]):
        self.b = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        i1 = account1 - 1
        if not (0 <= i1 < len(self.b)) :
            return False
        if self.b[i1] < money :
            return False

        i2 = account2 - 1
        if not (0 <= i2 < len(self.b)) :
            return False

        self.b[i2] += money
        self.b[i1] -= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        i = account - 1
        if not (0 <= i < len(self.b)) :
            return False
        self.b[i] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        i = account - 1
        if not (0 <= i < len(self.b)) :
            return False
        if money > self.b[i] :
            return False
        self.b[i] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)