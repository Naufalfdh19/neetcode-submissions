class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                temp *= nums[j]
                if temp > nums[i]:
                    nums[i] = temp
        
        return max(nums)
