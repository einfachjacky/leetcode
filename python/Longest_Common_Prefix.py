#Extremely ugly code for easy which only beats 5% but I am annoyed and dont wanna improve it now
import numpy as np
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        A = np.min(np.array([len(i) for i in strs]))
        if A==0:
            return s
        if len(strs)==1:
            return strs[0]
        for i in range(A):
            if all_equal([j[i] for j in strs]):
                s+=strs[0][i]
                if i+1==A:
                    return s
            else:
                return s
