class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            answer = max(answer, profit)

        return answer