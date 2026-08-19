class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0 
        win = 0
        max_avg = (float('-inf'))
        for r in range(len(nums)):
            win += nums[r]
            if r - l + 1 == k:
                max_avg = max(win/k,max_avg)
                win-=nums[l]
                l += 1 
        return max_avg
