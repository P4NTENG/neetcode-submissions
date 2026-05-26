class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        answer = 0
        patience = k
        for right in range(len(s)):
            if patience > 0 and s[right] != s[left]:
                patience -= 1
            elif patience == 0 and s[right] != s[left]:
                left += 1
                while s[left - 1] == s[left]:
                    left += 1
                patience = k

            answer = max(answer, right - left + 1)
        return answer