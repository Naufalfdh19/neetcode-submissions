class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:    

        dp = {len(s):True} 

        def dfs(idx):
            if idx in dp:
                return dp[idx]

            for word in wordDict:
                if s[idx:idx+len(word)] == word and idx+len(word) <= len(s):
                    if dfs(idx+len(word)):
                        dp[idx] = True
                        return True
                    dp[idx] = False
      

            return False

        return dfs(0)


