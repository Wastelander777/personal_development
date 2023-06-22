from typing import List


class Solution:
    def maxProfit(prices: List[int], fee: int) -> int:
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Solution.maxProfit(prices = [1,3,7,5,10,3], fee = 3)
