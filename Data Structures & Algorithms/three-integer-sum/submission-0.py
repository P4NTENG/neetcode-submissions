class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        answer.append(sorted([nums[i], nums[j], nums[k]]))

        return [list(x) for x in set(tuple(x) for x in answer)]