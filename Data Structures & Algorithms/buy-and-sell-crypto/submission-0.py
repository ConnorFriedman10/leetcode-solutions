class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 or not prices:
            return 0
        
        currmax = 0
        for idx, price in enumerate(prices[:-1]):
            if max(prices[idx+1:]) - price > currmax:
                currmax = max(prices[idx+1:]) - price

        return currmax

        