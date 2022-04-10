class Solution:
    def calPoints(self, ops: List[str]) -> int:
        n=len(ops)
        l=[]
        i=0
        while i<n:
            
            if ops[i]=="+":
                x=int(l.pop())
                y=int(l.pop())
                l.append(y)
                l.append(x)
                l.append(x+y)
            elif ops[i]=='D':
                x=int(l.pop())
                l.append(x)
                l.append(x*2)
            elif ops[i]=='C':
                l.pop()
            else:
                l.append(int(ops[i]))
            i+=1
            print(l)
    
        print(i)
        return sum(l)
            