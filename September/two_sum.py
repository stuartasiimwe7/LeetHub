class Solution(object):
    def twoSum(self, nums, target):
        index = {}
        for i in range(len(nums)):
            if(target - nums[i]) in index:
                return [index[target-nums[i]],i]
            index[nums[i]] = i