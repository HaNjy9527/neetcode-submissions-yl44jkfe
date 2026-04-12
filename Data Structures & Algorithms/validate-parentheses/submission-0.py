class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        a = []
        
        for i in range(len(s)):  # 用 for 更簡潔
            if s[i] in bracket_map:  # 閉括號
                if len(a) > 0 and a[-1] == bracket_map[s[i]]:
                    a.pop()
                else:
                    return False
            else:  # 開括號
                a.append(s[i])
        
        return len(a) == 0