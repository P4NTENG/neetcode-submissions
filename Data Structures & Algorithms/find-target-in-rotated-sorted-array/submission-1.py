class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (nums[left] <= target <= nums[mid]) or (
                nums[left] > nums[mid] and (target <= nums[mid] or target >= nums[left])
            ):
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1