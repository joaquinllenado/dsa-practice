class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(len(prices)):
            cur = prices[r] - prices[l]

            if cur > max_profit:
                max_profit = cur
            elif cur < 0:
                l = r

        return max_profit