class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, profit = 0, 1, 0
        maxProfit = 0

        while r < len(prices):
            print(prices[l], prices[r])
            if prices[l] >= prices[r]:
                l = r
                r = l + 1
            else: 
                profit = prices[r] - prices[l]
                if profit > maxProfit: maxProfit = profit
                r += 1
        
        return maxProfit