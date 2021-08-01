class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        res = 0

        if ruleKey == 'type':
            prop = 0
        elif ruleKey == 'color':
            prop = 1
        elif ruleKey == 'name':
            prop = 2
        
        for i in range(len(items)):
            if items[i][prop] == ruleValue:
                res+=1
                
        return res