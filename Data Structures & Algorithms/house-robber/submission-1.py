class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[-1])

        dp = {0:nums[0], 1:nums[1]}

        for i in range(2, len(nums)):
            temp = nums[i]+dp[i-2]
            for j in range(2, i+1):
                if temp < nums[i]+dp[i-j]: 
                    temp = nums[i]+dp[i-j]
            dp[i] = temp

        return max(dp.values())