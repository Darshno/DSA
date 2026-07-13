class Solution(object):
    def findMissingElements(self, nums):
        s = set(nums)
        res = []

        for x in range(min(nums), max(nums) + 1):
            if x not in s:
                res.append(x)

        return res