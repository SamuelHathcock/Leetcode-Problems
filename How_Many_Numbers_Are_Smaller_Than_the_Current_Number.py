'''
Given the array nums, for each nums[i] find out 
how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number 
of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''
L = [5,2,7,3,4,3,1,9,9,6]

print(sorted(L))
print(L)
class Solution(object):
    def smallerNumbersThanCurrent(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        D = {}
        N = sorted(nums)
        res = []
        for i in range(len(nums)):
            if N[i] not in D:
                D.update({N[i]: i})
        for num in nums:
            res.append(D.get(num))
        return res
        

