class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # min heap, max heap
        # (price, amount)
        sell_reqs, purchase_reqs = [], []
        for price, amount, order_type in orders :
            if order_type == 0 : # buy
                while sell_reqs and sell_reqs[0][0] <= price and amount > 0 :
                    seller_price, seller_amout = sell_reqs[0]

                    if seller_amout <= amount :
                        heappop(sell_reqs)
                    else :
                        sell_reqs[0][1] -= amount

                    amount = max(0, amount - seller_amout)

                if amount > 0 :
                    heappush(purchase_reqs, [-price, amount])
                continue
            
            # sell
            while purchase_reqs and -purchase_reqs[0][0] >= price and amount > 0 :
                purchaser_price, purchaser_amount = purchase_reqs[0]
                purchaser_price *= -1

                if purchaser_amount <= amount :
                    heappop(purchase_reqs)
                else :
                    purchase_reqs[0][1] -= amount

                amount = max(0, amount - purchaser_amount)

            if amount > 0 :
                heappush(sell_reqs, [price, amount])

        return (sum(x[1] for x in sell_reqs) + sum(x[1] for x in purchase_reqs)) % (10 ** 9 + 7)