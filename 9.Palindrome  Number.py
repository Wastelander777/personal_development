# URL of the  problem: https://leetcode.com/problems/palindrome-number/
# This submit works properly and beats 73.62% of them
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == (str(x)[::-1]):
            return True
        else:
            return False
