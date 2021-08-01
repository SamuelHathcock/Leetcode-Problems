"""
Given the head of a singly linked list, return true if it is a palindrome.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = ""
        while head.next != None:
            temp += head.next
        return temp == temp[::-1]