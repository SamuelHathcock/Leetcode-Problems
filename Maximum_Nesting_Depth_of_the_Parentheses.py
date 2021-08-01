class Solution(object):
    def maxDepth(self, s: str) -> int:
        if len(s) == 0: return 0
        res = cur = 0
        for char in s:
            if char == '(':
                cur += 1
                res = max(cur, res)
            elif char == ')':
                cur -= 1
        return res