'''
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
'''

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = start
        i = 1
        while i != n:
            res = res ^ (start + 2 * i)   
            i += 1            
        return res
        
S = Solution
print(S.xorOperation(S, 11, 5))

# My solution was faster than 96% of others!!!
