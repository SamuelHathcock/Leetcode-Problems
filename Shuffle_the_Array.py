'''
Given the array nums consisting of 2n elements in the form
 [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form 
[x1,y1,x2,y2,...,xn,yn].
'''
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        A = nums[:n]
        B = nums[n:]
        res = []
        for i in range(0, n):
            res.append(A[i])
            res.append(B[i])
        return res

#Simpler and faster Solution found in discussion
        '''
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
        '''
            