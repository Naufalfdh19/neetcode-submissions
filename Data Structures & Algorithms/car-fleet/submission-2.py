class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        state = []
        for i in range(n):
            state.append((position[i],speed[i]))

        state = sorted(state)

        res = 0
        stack = [state.pop()]

        seen = set()
        while stack and state:
            currPos, currSpeed = state.pop()
            currTime = self.calStep(target,currPos,currSpeed)
            prevTime =  self.calStep(target,stack[-1][0],stack[-1][1])
            
            if currTime <= prevTime: 
                stack = [(stack[-1][0],stack[-1][1])]
            else:
                res += 1
                seen.add((stack[-1][0],stack[-1][1]))
                stack = [(currPos, currSpeed)]

        if stack and (stack[-1][0],stack[-1][1]) not in seen:
            res += 1

        return res
    
    def calStep(self, target, pos, speed):
        return (target-pos)/speed