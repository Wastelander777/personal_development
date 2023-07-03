# URL to the problem solved below:
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        integer = {1,5,10,50,100,500,1000}
        roman = {'I','V','X','L','C','D','M'}
        output = 0
        for x,y in s:
            print(x,y)
