class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False]*len(nums)


        def backtrack(bucket,visited):
            if len(bucket) == len(nums):
                res.append(bucket)
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    backtrack(bucket+[nums[i]], visited)
                    visited[i] = False
            
        backtrack([],visited)
        
        return res
                

            
            
            