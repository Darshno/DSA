class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i,num in enumerate(nums):
            left = target-num
            if left in s:
                return[s[left],i]
            s[num] =i

            
        