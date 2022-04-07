from sortedcontainers import SortedList

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==0:
            return 0
        s=SortedList(stones)
        while len(s)>=2:
            y=s.pop()
            x=s.pop()
            if y!=x:
                s.add(y-x)
        if len(s):
            return s.pop()
        else: return 0
            