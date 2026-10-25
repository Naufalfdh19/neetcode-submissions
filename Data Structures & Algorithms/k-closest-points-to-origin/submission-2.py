class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceMap = {}

        for i in range(len(points)):
            point = points[i]
            x, y = point[0], point[1]
            distance = math.sqrt(x**2+y**2)
            distanceMap[i] = distance
        
        distanceList = sorted(list(distanceMap.items()), key=lambda x:x[1])

        res = []
        for i in range(k):
            idx = distanceList[i][0]
            res.append(points[idx])

        return res

        

