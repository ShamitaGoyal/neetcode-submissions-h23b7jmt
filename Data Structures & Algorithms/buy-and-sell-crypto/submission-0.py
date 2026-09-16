class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] #10 
        best_profit = 0

        for p in prices:
            profit = p - min_price # 10 - 10 = 0, 1 - 0=1, 5, 6
            best_profit = max(best_profit, profit) #bp=0,5 1, 
            min_price = min(min_price, p) #mp=0, 0, 

        return best_profit 