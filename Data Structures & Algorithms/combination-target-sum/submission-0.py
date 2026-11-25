class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        dpbool = [False]*(target+1)
        dp = [[] for _ in range(target+1)]

        dpbool[0] = True

        seen = set()
        for i in range(target+1):
            for num in nums:
                if num > i:
                    continue

                prev = i-num
  
                if dpbool[prev]:
                    for prefixList in dp[prev]:
                        sortedList = sorted(prefixList+[num])
                        if tuple(sortedList) not in seen:
                            dp[i].append(sortedList)
                            seen.add(tuple(sortedList))
                if prev == 0:
                    dp[i].append([num])

                if len(dp[i]) > 0:
                    dpbool[i] = True
                
        return dp[-1]




