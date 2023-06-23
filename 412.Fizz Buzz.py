from typing import List
# URL to the listed problem: https://leetcode.com/problems/fizz-buzz/

# This submits works properly and beats 66.52% of thems lets goooo
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = []

        for x in range(1, n + 1):
            if ((x % 3 == 0) and (x % 5 != 0)):
                answer.append("Fizz")
            elif ((x % 5 == 0) and (x % 3 != 0)):
                answer.append("Buzz")
            elif ((x % 3 == 0) and (x % 5 == 0)):
                answer.append("FizzBuzz")
            else:
                answer.append(str(x))
        return answer