class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        mat = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            mat[i][0] = i
        for j in range(n + 1):
            mat[0][j] = j
        print(mat)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    mat[i][j]=mat[i-1][j-1]
                else:
                    x = min(mat[i][j-1],mat[i-1][j],mat[i-1][j-1])
                    mat[i][j]=x+1
        return mat[-1][-1]
        