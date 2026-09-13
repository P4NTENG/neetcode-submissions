class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        under_k = nums[:k]
        heapq.heapify(under_k)

        for num in nums[k:]:
            if num > under_k[0]:
                heapq.heappushpop(under_k, num)

        return under_k[0]
