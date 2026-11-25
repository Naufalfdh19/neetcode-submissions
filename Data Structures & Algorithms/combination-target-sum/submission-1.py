class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        dp[0] = [[]]

        for num in nums:
            for total in range(num,target+1):
                for combination in dp[total-num]:
                    dp[total].append(combination+[num])
        
        return dp[target]





