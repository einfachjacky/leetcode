import numpy as np
class Solution:
    def reverse(self, x: int) -> int:
        xout = np.sign(x)*int(str(np.abs(x))[::-1])
        if xout<-2**31 or xout>2**31-1:
            return 0
        else:
            return xout
