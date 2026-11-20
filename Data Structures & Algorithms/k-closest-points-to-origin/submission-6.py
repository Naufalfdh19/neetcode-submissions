class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []
        for point in points:
            x1, y1 = point
            distance = math.sqrt(x1**2+y1**2)
            distances.append((distance,point))
        
        heapq.heapify(distances)

        res = []
        while k > 0:
            _, point = heapq.heappop(distances)
            # print(distances, point)
            res.append(point)
            k -= 1

        return res
            