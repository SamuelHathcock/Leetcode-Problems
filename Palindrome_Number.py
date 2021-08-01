"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
 For example, 121 is palindrome while 123 is

"""

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        # x = str(x)
        # if(x == x[::-1]):
        #     return True
        # else: return False
        
        if x < 0: return False

        x_ = x
        newNum = 0
        while x_ > 0:
            newNum = newNum * 10 + x_ % 10
            x_ = x_//10
        return newNum == x
        
