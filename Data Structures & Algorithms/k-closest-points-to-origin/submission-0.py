class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for cord in points:
            x,y = cord
            dist = math.sqrt(x**2 + y**2)
            minHeap.append([dist,x,y])
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            point = heapq.heappop(minHeap)
            d,x,y = point
            res.append([x,y])
            k -= 1
        return res
        