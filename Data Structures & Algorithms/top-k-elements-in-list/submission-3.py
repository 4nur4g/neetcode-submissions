class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mh = []
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        for num, freq in freq.items():
            bucket = (freq,num)
            heapq.heappush(mh,bucket)
            if len(mh) > k:
                heapq.heappop(mh)
        return [j for i,j in mh]

       