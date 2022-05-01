class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls=[]
        lt=[]
        for i in s:
            if i == '#':
                if len(ls):
                    ls.pop()
            else:
                ls.append(i)
        for i in t:
            if i=='#':
                if len(lt):
                    lt.pop()
            else:
                lt.append(i)
        print(ls)
        print(lt)
        if ls==lt:
            return True
        else:
            return False