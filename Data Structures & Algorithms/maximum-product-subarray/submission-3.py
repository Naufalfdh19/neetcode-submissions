class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxDp = [num for num in nums]
        minDp = [num for num in nums]

        for i in range(n):
            if i != 0:
                maxDp[i] = max(nums[i]*maxDp[i-1], nums[i], nums[i]*minDp[i-1])
                minDp[i] = min(nums[i]*minDp[i-1], nums[i], nums[i]*maxDp[i-1])
        
        return max(max(minDp), max(maxDp))
            
    
