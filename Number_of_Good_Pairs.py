'''
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
'''
class Solution(object):
    def numIdenticalPairs(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        D = {}
        res = 0
        for num in nums:
            if num in D:
                D[num]+=1
                res+=D[num]
            else:
                D.update({num: 0})
        return res

#Fastest solution in discussion
'''
        pairs = 0
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for num in d:
            val = d[num]
            for i in range(val):
                pairs += i
        return pairs
'''

        