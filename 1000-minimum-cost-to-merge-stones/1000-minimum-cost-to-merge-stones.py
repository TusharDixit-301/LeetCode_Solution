class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        #min dp x,y , dp[x][mid]+dp[mid+1][y]
        
        n = len(stones)
        if (n-1)%(k-1):
            return -1
        cum_sum = [0]
        for stone in stones:
            cum_sum.append(cum_sum[-1]+stone)
        #print(cum_sum)
        
        dp = [[0]*n for _ in range(n)]
        #print(dp)
        
        for itr in range(k-1,n):
            for x in range(n):
                y = x + itr
                if y>n-1:
                    break
                if itr == (k-1):
                    dp[x][y]=cum_sum[y+1] - cum_sum[x]
                else:
                    dp[x][y] = float('inf')
                    for mid in range(x,y,k-1):
                        dp[x][y] = min(dp[x][y], dp[x][mid]+dp[mid+1][y])
                    if itr%(k-1) == 0:
                        dp[x][y]+= cum_sum[y+1]- cum_sum[x]
        return dp[0][n-1]