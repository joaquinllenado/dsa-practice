class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_prof = 0

        for r in range(len(prices)):
            cur = prices[r] - prices[l]

            if cur > max_prof:
                max_prof = cur

            if prices[r] < prices[l]:
                l = r
        
        return max_prof