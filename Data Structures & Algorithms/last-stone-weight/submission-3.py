class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]


        weight_heap = [-s for s in stones]
        heapq.heapify(weight_heap)

        while len(weight_heap) > 1:

            heaviest = - heapq.heappop(weight_heap)
            s_heaviest = -heapq.heappop(weight_heap)

            if heaviest != s_heaviest:
                heapq.heappush(weight_heap, -(heaviest-s_heaviest))
            
    
        return 0 if not weight_heap else - weight_heap[0]


        
        