class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_set = sorted(nums_set)
        print(nums_set)
        streak = 1
        longest = 1
        for i in range(1, len(nums_set)):
            if nums_set[i] == nums_set[i-1] + 1:
                streak += 1
            else:
                streak = 1
            if streak > longest:
                longest = streak
        return longest