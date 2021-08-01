"""
The string "PAYPALISHIRING" is written in a 
zigzag pattern on a given number of rows like 
this: (you may want to display this pattern in
 a fixed font for better legibility)
"""

class Solution(object):
    def convert(self, s, numRows):   
        if numRows == 1 or numRows > len(s):
            return s

        temp = [''] * numRows
        index = 0
        increment = 1

        for char in s:
            temp[index] += char

            if index == 0:
                increment = 1
            elif index == numRows - 1:
                increment = -1
            
            index += increment

        return ''.join(temp)



S = Solution()
print(S.convert("PAYPALISHIRING", 3))


