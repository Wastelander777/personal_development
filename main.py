from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        seq = []

        # seq += [(nums[i + 1] - nums[i]) for i in range(1,len(nums)-1)]
        for i in range(0, len(nums)-1):
            diff = nums[i + 1] - nums[i]
            if nums[i + 1] - nums[i] == diff:
                seq.append(nums[i])
        return seq

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Solution.longestArithSeqLength(None,[3,6,9,12]))
    print("Thanks for using it! Visit my github: https://github.com/Wastelander777"
          "\nMade by Pablo Ugarte")
