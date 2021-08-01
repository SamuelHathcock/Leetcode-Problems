'''
Given the array candies and the integer extraCandies, 
where candies[i] represents the number of candies that 
the ith kid has.

For each kid check if there is a way to distribute 
extraCandies among the kids such that he or she can have 
the greatest number of candies among them. Notice that 
multiple kids can have the greatest number of candies.
'''

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        moox = max(candies)
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= moox:
                res.append(True)
            else:
                res.append(False)
        return res
    
#Leetcode Discussion 2 Liner Solution that is also very fast
'''
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        return [candy + extraCandies >= M for candy in candies]
'''

