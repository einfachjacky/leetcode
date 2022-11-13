#commented code works, however it is too slow. Bisection scales better
import bisect
class MedianFinder:
    def __init__(self):
        self.l = []
        
    def addNum(self, num: int) -> None:
        bisect.insort(self.l, num)
        return None
        #if len(self.l)>0:
        #    for i in range(len(self.l)):
        #        if num>self.l[i]:
        #            continue
        #        else:
        #            self.l = self.l[:i]+[num]+self.l[i:]
        #            break
        #    if i==len(self.l)-1:
        #        self.l.append(num)
        #else:
        #    self.l = [num]
        #return None

    def findMedian(self) -> float:
        length = len(self.l)
        if length%2==1:
            return self.l[length//2]
        else:
            return (self.l[length//2-1]+self.l[length//2])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
