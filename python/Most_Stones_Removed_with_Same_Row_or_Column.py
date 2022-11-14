import numpy as np
from itertools import filterfalse
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xmax = np.max([stone[0] for stone in stones])
        ymax = np.max([stone[1] for stone in stones])
        wall = np.zeros((xmax+1, ymax+1))
        for stone in stones:
            wall[stone[0], stone[1]]=1
        Cmax_f=0
        Cmax=0
        stones_removed = []
        clx =[]
        cly = []
        for stone in stones[:]:
            clx.append(stone[0])
            cly.append(stone[1])
            stones_removed.append(stone)
            try:
                stones.remove(stone)
            except:
                continue
            Cmax+=1
            
            while len(clx)>0 or len(cly)>0:
                for x in clx[:]:
                    for stone_x in stones[:]:
                        
                        if stone_x[0]==x:
                            cly.append(stone_x[1])
                            stones_removed.append(stone_x)
                            stones.remove(stone_x)
                            Cmax+=1
                    clx.remove(x)
                
                for y in cly[:]:
                    for stone_y in stones[:]:
                        if stone_y[1]==y:
                            clx.append(stone_y[0])
                            stones_removed.append(stone_y)
                            stones.remove(stone_y)
                            Cmax+=1
                    cly.remove(y)
            Cmax-=1
        return Cmax

