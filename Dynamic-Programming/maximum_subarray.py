""" Leet Code Solution # 53 :   Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Algorithm : Dynamic Programming , Divide & Conquer

Time and Space Complexity : TBD
"""
from typing import List
nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:

    """ Solution - I """
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i]+=nums[i-1]
        return max(nums)


ins=Solution()
print(ins.maxSubArray(nums))