class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        reserve = {}
        n = len(s2)

        for char in s1:
            if char not in reserve:
                reserve[char] = 0
            reserve[char] += 1

        temp = reserve.copy()
        l, r = 0, 0
        while r < n:
            left = s2[l]
            right = s2[r]

            if not any(temp.values()):
                return True

            if right in temp:
                print(left, right, temp)
                if temp[right] == 0:
                    while s2[l] != s2[r]:
                        temp[s2[l]] += 1
                        l += 1
                else:
                    temp[right] -= 1

                if left not in temp:
                    l = r
            else:
                temp = reserve.copy()
            
            r += 1
        
        if not any(temp.values()):
            return True

        return False