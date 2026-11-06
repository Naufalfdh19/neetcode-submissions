class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = len(s)

        longestSubstring = float("-inf")
        for prev in chars:
            l, r = 0, 0
            
            tempK = k
            while r < n:
                curr = s[r]
                if curr != prev and tempK > 0:
                    tempK -= 1
                    r += 1
                elif curr == prev:
                    r += 1
                else:
                    if s[l] != prev:
                        tempK += 1
                    l += 1

                if r-l > longestSubstring:
                    longestSubstring = r-l
        
        return longestSubstring
                
                    
            


        