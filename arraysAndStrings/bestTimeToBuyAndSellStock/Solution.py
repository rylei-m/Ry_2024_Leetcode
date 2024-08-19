from pyparsing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > 0:
                    maxProfit = max(maxProfit, profit)

        return maxProfit if maxProfit > float('-inf') else 0


prices = [7,1,5,3,6,4]