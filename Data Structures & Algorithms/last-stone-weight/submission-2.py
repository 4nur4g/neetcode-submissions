class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0

        weight_heap = [-s for s in stones]
        heapq.heapify(weight_heap)

        while len(weight_heap) > 1:

            heaviest = -weight_heap[0]
            heapq.heappop(weight_heap)

            s_heaviest = -weight_heap[0]
            heapq.heappop(weight_heap)

            if heaviest == s_heaviest:
                continue
            elif heaviest > s_heaviest:
                heapq.heappush(weight_heap,-(heaviest - s_heaviest))
            else: 
                heapq.heappush(weight_heap,-(- heaviest + s_heaviest))
        if len(weight_heap) > 0:
            return -weight_heap[0]
        return 0


        
        