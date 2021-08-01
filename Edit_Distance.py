'''
Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character
'''

class Solution(object):
    def minDistance(self, w1: str, w2: str) -> int:
        for i in range(0, len(w1)):
            if (w1[i] == w2[i]):
                


    # def minDistance(self, w1: str, w2: str) -> int:
    #     if len(w1) > len(w2):
    #         protocol1(w1, w2)
    #     if len(w1) < len(w2):
    #         protocol2(w1, w2)
    #     else:
    #         protocol3(w1, w2)

    # def protocol1(word1: str, word2: str):
    #     same = findSame(w1, w2)

    
    # def protocol2(word1: str, word2: str):
    #     same = findSame(w1, w2)


    # def protocol3(word1: str, word2: str):
    #     same = findSame(w1, w2)



    # def findSame(word1: str, word2: str):
    #     w1 = word1
    #     w2 = word2
    #     dicc = {}
    #     for i in range(0, len(w1)):
    #         if w1[i] in w2: 
    #             w2index = w2.index[w1[i]]
    #             dicc[(w1[i], i)] = (w2[i], i)
    #             w2[w2index] = ''
    #     return dicc



