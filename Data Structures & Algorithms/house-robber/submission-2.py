class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[-1])

        dp = {0:nums[0],1:nums[1]}

        maximumMoney = nums[0]

        for i in range(2, len(nums)): 
            dp[i] = nums[i] + maximumMoney
            maximumMoney = max(dp[i-2], dp[i-1])

        return max(dp.values())