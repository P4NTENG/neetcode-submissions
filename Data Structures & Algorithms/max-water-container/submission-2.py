class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            curr_area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, curr_area)

            if heights[left] < heights[right]:
                prev_left = left
                while left < right and heights[left] <= heights[prev_left]:
                    left += 1
            else:
                prev_right = right
                while right > left and heights[right] <= heights[prev_right]:
                    right -= 1

        return max_area