class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            letter = s[i]
            if i+1<len(s):
                nextletter=s[i+1]
            else:
                nextletter=None
            if letter=="I":
                if nextletter=="V" or nextletter=="X":
                    res-=1
                else:
                    res+=1
            elif letter=="V":
                res+=5
            elif letter=="X":
                if nextletter=="L" or nextletter=="C":
                    res-=10
                else:
                    res+=10
            elif letter=="L":
                res+=50
            elif letter=="C":
                if nextletter=="D" or nextletter=="M":
                    res-=100
                else:
                    res+=100
            elif letter=="D":
                res+=500
            elif letter=="M":
                res+=1000
            else:
                print("Error")
            #print(i, "letter=", letter, " nextletter=", nextletter, " res=", res)
            if nextletter is None:
                return res
