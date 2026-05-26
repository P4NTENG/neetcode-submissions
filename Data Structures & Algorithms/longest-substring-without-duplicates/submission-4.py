class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        word_counter = set()
        for right in range(len(s)):
            while s[right] in word_counter:
                word_counter.remove(s[left])
                left += 1

            word_counter.add(s[right])
            answer = max(answer, right - left + 1)

        return answer