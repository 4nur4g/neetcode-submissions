class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = Counter(tasks)
        maxHeap = [-i for i in freqMap.values()]
        heapq.heapify(maxHeap)
        q = deque()
        t = 0

        while q or maxHeap:
            t += 1
            if maxHeap:
                num = heapq.heappop(maxHeap)
                if num:
                    if num + 1 < 0:
                        # [num,time]
                        q.append([num + 1, t + n])
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t
            
            
            

        
        
        