from pyparsing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')

        for price in prices:
            if price < minPrice:
               minPrice = price

            profit = price - minPrice
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit


prices = [7, 1, 5, 3, 6, 4]
