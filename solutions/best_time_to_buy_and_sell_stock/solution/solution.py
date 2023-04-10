class Solution:
    def max_profit(self, prices: list[int]) -> int:
        monetary_gain = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                monetary_gain = max(price - min_price, monetary_gain)

        return monetary_gain
