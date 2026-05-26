class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = [a.lower() for a in s if a.isalpha()]
        for i in range(0, len(alpha_s)//2):
            if alpha_s[i] != alpha_s[len(alpha_s)-1-i]:
                return False
        return True