class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num in frequency.keys():
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        most_frequent = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        most_frequent = [s[0] for s in most_frequent[0:k]]

        return most_frequent