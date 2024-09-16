from heapq import heappush, heappop, heapify

class MedianFinder:
    def __init__(self):
        # Initializes the MedianFinder object with two heaps:
        # - self.left: a max-heap (inverted to use Python's min-heap) for the lower half of the numbers.
        # - self.right: a min-heap for the upper half of the numbers.
        self.left = []  # Max-heap to store the smaller half of the numbers 
        self.right = []  # Min-heap to store the larger half of the numbers

    def addNum(self, num: int) -> None:
        # Adds a number to the data structure.
        # - Uses the heaps to keep track of the median.
        
        # If left heap is empty or the new number is less than or equal to the maximum number in the left heap
        if len(self.left) == 0 or -self.left[0] >= num:
            # Add the number to the left heap (inverted to maintain max-heap properties)
            heappush(self.left, -num)
        else:
            # Otherwise, add the number to the right heap
            heappush(self.right, num)

        # Rebalance the heaps if their sizes differ by more than 1
        if abs(len(self.left) - len(self.right)) > 1:
            # If the left heap has more elements, move the maximum from left to right
            if len(self.left) > len(self.right):
                # Pop the maximum element from the left heap (inverted back to positive)
                obj = -heappop(self.left)
                # Push the element to the right heap
                heappush(self.right, obj)
            else:
                # If the right heap has more elements, move the minimum from right to left
                obj = heappop(self.right)
                # Push the element to the left heap (inverted to maintain max-heap properties)
                heappush(self.left, -obj)

    def findMedian(self) -> float:
        """
        Returns the median of the numbers added so far.
        """
        # If the heaps are of equal size, median is the average of the roots of both heaps
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        # If the left heap has more elements, the median is the root of the left heap
        elif len(self.left) > len(self.right):
            return -self.left[0]
        # Otherwise, the median is the root of the right heap
        else:
            return self.right[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
