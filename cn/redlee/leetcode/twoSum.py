"""
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class twoSum(object):
    @classmethod
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[i + 1:]:
                return [i, nums.index(target - nums[i], i + 1)]


nums = [3, 3]
target = 6
x = twoSum.twoSum(nums, target)
print(x)
