import heapq

class MedianFinder:
    def __init__(self):
        # max_heap: left half (smaller numbers)
        # Python has no max-heap, so we NEGATE values
        self.max_heap = []  # stores negated values

        # min_heap: right half (larger numbers)
        self.min_heap = []  # stores actual values

    def addNum(self, num: int) -> None:
        # Step 1: push to max_heap first (negate!)
        heapq.heappush(self.max_heap, -num)

        # Step 2: fix ordering — max of left ≤ min of right
        if (self.min_heap and
            -self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Step 3: rebalance sizes (differ by at most 1)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        # odd total: larger heap holds the middle
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        if len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])

        # even total: average of two middle elements
        return (-self.max_heap[0] + self.min_heap[0]) / 2