class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        n = len(nums)
        nums.sort()

        seen = set()
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                if nums[i]+nums[l]+nums[r] < 0:
                    l += 1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                else:
                    if (nums[i],nums[l],nums[r]) not in seen:
                        seen.add((nums[i],nums[l],nums[r]))    
                    r -= 1       
        
        result = list(seen)

        return result


