class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while right - left > 1:
            mid = (right + left) // 2
            if nums[mid] < nums[right]:
                right = mid  # 왼쪽 선택
            else:
                left = mid  # 오른쪽 선택

        return nums[left]