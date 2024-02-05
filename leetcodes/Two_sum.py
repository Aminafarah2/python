# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

class Solution(object):
    def twoSums(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_num = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict_num:
                return [dict_num[complement], i]
            dict_num[num] = i
        return None

# Example usage:
nums_list = [2, 7, 11, 15]
target_value = 9

# Create an instance of the Solution class
solution_instance = Solution()

# Call the twoSums method using the instance
result = solution_instance.twoSums(nums_list, target_value)
print(result)
