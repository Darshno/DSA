class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        winsum = 0
        min_size = float('inf')
        for r in range(len(nums)):
            winsum += nums[r]
            while winsum >= target:
                min_size = min(min_size,r-l+1)
                winsum -= nums[l]
                l += 1
        return 0 if min_size == float('inf') else min_size