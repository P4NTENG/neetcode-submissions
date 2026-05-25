class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = [a.lower() for a in s if a.isalnum()]
        return alpha_s == alpha_s[::-1]