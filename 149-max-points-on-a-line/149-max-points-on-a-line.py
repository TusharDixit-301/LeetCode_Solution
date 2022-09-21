def xyz(p1,p2):
    x1,y1=p1
    x2,y2=p2
    if x1==x2:
        return float("inf")
    else:
        return (y2-y1)//(x2-x1)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res=0
        n=len(points)
        if n<=2:
            return n
        for i in range(n):
            d={}
            for j in range(i+1,n):
                if points[j][0] == points[i][0]:
                    slope = float("inf")
                else: 
                    slope = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                if slope in d:
                    d[slope]+=1
                else:
                    d[slope]=1
                res=max(res,d[slope])
        return res+1