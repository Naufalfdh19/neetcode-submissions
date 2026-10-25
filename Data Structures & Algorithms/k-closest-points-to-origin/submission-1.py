class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [math.sqrt((coor[0]**2 + coor[1]**2)) for coor in points]
        heapq.heapify(distance)

        res = []
        while len(res) < k:
            for coor in points:
                if math.sqrt((coor[0]**2 + coor[1]**2)) == distance[0]:
                    res.append(coor)
            heapq.heappop(distance)
        
        return res
        
        

        return res