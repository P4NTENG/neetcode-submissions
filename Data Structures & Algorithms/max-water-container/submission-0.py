class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0

        for i in range(0, len(heights)-1):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j-i)
                answer = max(answer, area)

        return answer