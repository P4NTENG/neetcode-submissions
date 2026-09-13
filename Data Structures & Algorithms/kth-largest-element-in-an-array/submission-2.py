class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        under_k = [0] * k

        for num in nums:
            if num > min(under_k):
                under_k[under_k.index(min(under_k))] = num

        return min(under_k)
