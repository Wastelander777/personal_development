from typing import List

# URL to the problem solved below:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

class Solution:

    # This was my first aproach, but it was not working properly
    def maxProfitNotWorking(prices: List[int], fee: int) -> int:
        result = []
        bought = False

        for day_price in range(0,len(prices)):
            if not bought and (day_price != len(prices)-1):
                result.append(prices[day_price])
                bought = True
            elif bought and (abs(result[-1] - prices[day_price]) - fee) > 0:
                result.append(prices[day_price])
                bought = False

        return sum([(result[i + 1] - result[i]) - fee for i in range(0, len(result)-1, 2)])

    # This solution works properly and beats 89.61% of users lets gooooo
    def maxProfit(self, prices: List[int], fee: int) -> int:
        notHold, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            hold = max(hold, notHold - prices[i])
            notHold = max(notHold, hold + prices[i] - fee)
        return notHold