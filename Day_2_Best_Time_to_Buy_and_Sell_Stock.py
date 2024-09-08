# Challenge 2 — Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example:Input: prices = [7,1,5,3,6,4] Output: 5 Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

#721 ms 27.4 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]  # Buying Price
        y = 0  # Profit
        for i in range(1,len(prices)):
            x = min(x,prices[i])
            if prices[i]-x>y:
                y=prices[i]-x
        return y
      
