class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 0
        for i in range(0, len(nums)):
            temp += nums[i]
            nums[i] = temp
        return nums

l = [1, 2, 3, 4, 5]
s = Solution
print(s.runningSum(s, l))

