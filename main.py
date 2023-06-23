from typing import List

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

    def maxProfit(self, prices: List[int], fee: int) -> int:
        notHold, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            hold = max(hold, notHold - prices[i])
            notHold = max(notHold, hold + prices[i] - fee)
        return notHold


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Solution.maxProfit(None,[1,3,7,5,10,3], 3))
    print("Thanks for using it! Visit my github: https://github.com/Wastelander777")
