class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 只保留字母和數字，轉小寫
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        l = len(s)
        for i in range(l // 2):
            if s[i] != s[l - i - 1]:
                return False
        return True