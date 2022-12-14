class Solution(object):
    def twoSum(self, nums, target):
        buffer_dictionary = {}
        for i in range(nums):
            if nums[i] in buffer_dictionary:
                # if a number shows up in the dictionary already that means the
                return [buffer_dictionary[nums[i]], i]
                # necesarry pair has been iterated on previously
            else:  # else is entirely optional
                buffer_dictionary[target - nums[i]] = i
                # we insert the required number to pair with should it exist later in the list of numbers
