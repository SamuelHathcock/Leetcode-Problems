class Solution(object):
    def checkIfPangram(self, sentence: str) -> bool:
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet = set()
        for i in range(65,91):
            alphabet.add(chr(i))
        
        sentence = set(sentence.upper())
        
        if( len(alphabet.intersection(sentence)) == len(alphabet) ):
            return True
        return False

S = Solution()

S.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")

# Leetcode solution that's so simple I feel stupid now

        #return len(set(sentence)) == 26