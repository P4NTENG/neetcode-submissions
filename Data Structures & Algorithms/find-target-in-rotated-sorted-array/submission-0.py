class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (nums[mid] < nums[right] and nums[mid] < target <= nums[right]) or (
                nums[mid] > nums[right] and target <= nums[right]
            ):
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1