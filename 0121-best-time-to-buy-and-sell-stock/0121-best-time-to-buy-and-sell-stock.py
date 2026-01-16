class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        minimum_price = prices[0]
        maximum_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < minimum_price:
                minimum_price = prices[i]

            else:
                profit = prices[i] - minimum_price
                if profit > maximum_profit:
                    maximum_profit = profit

        return maximum_profit