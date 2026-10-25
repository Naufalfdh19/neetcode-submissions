class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pilesLen = len(piles)
        if h == pilesLen:
            return max(piles)
        
        checkK = {}
        lowerBound, higherBound = 1, max(piles)
        res = max(piles)
        while True:
            k = lowerBound+(higherBound-lowerBound)//2
            count = 0
            for pile in piles:
                count += math.ceil(pile/k)
            if count > h:
                lowerBound = k
            else:
                higherBound = k
                if k < res:
                    res = k

            if k in checkK:
                break
            checkK[k] = True
            

        return res
            
        


        

