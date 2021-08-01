'''
You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)"
in some order. The Goal Parser will interpret "G" as the string 
"G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.
'''

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = ''
        for i in range(0, len(command)):
            if command[i] == 'G':
                res+='G'
            elif command[i] == '(' and command[i+1] == ')':
                res+='o'
                i+=1
            elif command[i] == '(' and command[i+1] == 'a' and command[i+2] == 'l':
                res+='al'
                i+=2
        return res
        