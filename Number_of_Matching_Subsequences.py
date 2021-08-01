'''
Given a string s and an array of strings words, return the number of
 words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original
 string with some characters (can be none) deleted without changing 
 the relative order of the remaining characters.
'''


from collections import defaultdict


class Solution(object):
    def numMatchingSubseq(self, s: str, words: list) -> int:
        res = 0
        for word in words:
            if word[0] in s:
                lowerS = s.index(word[0]) + 1
                for i in range(1, len(word)):
                    for j in range(lowerS, len(s)):
                        if (word[i] == s[j]):
                            pass


S = Solution()
print('\n', 'Result: ', S.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))