class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)

        for task in tasks:
            counter[task] += 1
        
        tasks = [-val for _, val in counter.items()]
        heapq.heapify(tasks)

        queue = deque()
        time = 0
        remaining = 0
        while tasks or queue:
            time += 1

            remaining = 1 + heapq.heappop(tasks) if tasks else 0

            if remaining < 0:
                queue.append((time+n,remaining))
            
            if queue and queue[0][0] <= time:
                heapq.heappush(tasks, queue[0][1])
                queue.popleft()
        
        return time



        
        