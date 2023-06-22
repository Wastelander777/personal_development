from typing import List

# URL to the problem solved below:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = []
        bought = False
        for day_price in range(1,len(prices)):
            if not bought:
                result.append(prices[day_price])
                bought = True
            elif ((result[-1] - day_price) - fee) > 0:
                result.append(prices[day_price])
