import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (store negative values)
        self.large = []  # Min heap

    def small_to_large(self):  
        val = -1 * heapq.heappop(self.small)  # Get the max element from small
        heapq.heappush(self.large, val)       # Push it to large (min heap)

    def large_to_small(self):  
        val = heapq.heappop(self.large)      # Get the min element from large
        heapq.heappush(self.small, -1 * val) # Push it to small (max heap)

    def addNum(self, num: int) -> None:
        # Always push to max heap (small)
        heapq.heappush(self.small, -1 * num)

        # Ensure max(small) <= min(large)
        if self.large and (-self.small[0] > self.large[0]):
            self.small_to_large()

        # Balance the heaps
        if len(self.small) > len(self.large) + 1:
            self.small_to_large()
        elif len(self.large) > len(self.small):
            self.large_to_small()

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return ((-1 * self.small[0]) + self.large[0]) / 2