from heapq import heappush,heappop,heapify
class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]
        
    def addNum(self, num: int) -> None:
        if len(self.left)==0 or -1*self.left[0]>=num:
            heapq.heappush(self.left,-1*num)
        else:
            heapq.heappush(self.right,num)
        
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                obj = -heapq.heappop(self.left)
                heapq.heappush(self.right, obj)
            else:
                obj = heapq.heappop(self.right)
                heapq.heappush(self.left, -obj) 
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()