class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1: return 1
        # elif len(s) == 0: return None
        # usedchar = {}
        # count = 0
        # for i, char in enumerate(s):
        #     if char not in usedchar:
        
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            used[c] = i
        return max_length

s = "adfgdfbcvbghgggbvcvvgthyju"       
S = Solution()
print(S.lengthOfLongestSubstring(s))
            
            