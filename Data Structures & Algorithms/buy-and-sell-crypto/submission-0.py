class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        max_profit = 0 
        min_price = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - min_price)
            min_price = min(min_price, sell)
        
        return max_profit

