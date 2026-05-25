class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range (len(prices)-1):
            answer = max(max(prices[i+1:]) - prices[i], answer)

        return answer