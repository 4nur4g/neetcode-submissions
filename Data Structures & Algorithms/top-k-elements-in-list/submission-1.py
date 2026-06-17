class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] = freq[n] + 1
        heap = []
        for n, f in freq.items():
            heapq.heappush(heap,(f,n))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for freq, num in heap:
            res.append(num)
        return res 



        