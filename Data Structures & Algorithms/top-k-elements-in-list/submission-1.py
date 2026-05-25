class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        most_frequent = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        answer = [s[0] for s in most_frequent[0:k]]

        return answer