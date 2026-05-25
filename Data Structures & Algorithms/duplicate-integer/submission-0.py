class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = dict()
        for num in nums:
            if num in duplicate.keys():
                return True
            else:
                duplicate[num] = 1
        return False
        