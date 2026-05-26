class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        substring = s[0]
        max_length = 1

        for i in range(1, len(s)):
            if s[i] in substring:
                for index, character in enumerate(substring):
                    if character == s[i]:
                        substring = substring[i:]
            else:
                substring += s[i]
            max_length = max(max_length, len(substring))

        return max_length