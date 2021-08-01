'''
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith 
position moves to indices[i] in the shuffled string.
Return the shuffled string.
'''

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        D = {}
        res = ''
        for i in range(0, len(indices)):
            D.update({indices[i]: s[i]})
        for i in range(0, len(indices)):
            res+=D[i]
        return res