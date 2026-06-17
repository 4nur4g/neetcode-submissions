class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_nums = nums
        self.k = k
        heapq.heapify(self.heap_nums)
        while len(self.heap_nums) > k:
            heapq.heappop(self.heap_nums)

    def add(self, val: int) -> int:
        if len(self.heap_nums) < self.k:
            heapq.heappush(self.heap_nums, val)
        else:
            heapq.heappushpop(self.heap_nums,val)
        return self.heap_nums[0]
        
