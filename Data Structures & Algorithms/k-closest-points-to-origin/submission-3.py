class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceList = []
        

        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt(x**2+y**2)
            distanceList.append((distance, point))
        
        heapq.heapify(distanceList)

        res = []
        for i in range(k):
            res.append(distanceList[0][1])
            heapq.heappop(distanceList)

        return res

        

