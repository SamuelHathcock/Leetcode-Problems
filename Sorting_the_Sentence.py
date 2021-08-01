'''
A sentence is a list of words that are separated by a single 
space with no leading or trailing spaces. 
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word 
position to each word then rearranging the words in the
sentence.
'''

class Solution(object):
    def sortSentence(self, s: str) -> str:
        sArr = s.split()

        sArr.sort(key = lambda x: x[-1])

        res = ""
        for word in sArr:
            res += word.replace(word[-1], ' ')
        res = res[:-1]

        return res

S = Solution
print(S.sortSentence(S, "Myself2 Me1 I4 and3"))

