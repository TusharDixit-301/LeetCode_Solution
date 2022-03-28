class Solution:
    def transpose(self,mat):
        for i in range(len(mat)):
            for j in range(i+1,len(mat[i])):
                mat[j][i],mat[i][j]=mat[i][j],mat[j][i]
        self.reverseEachRow(mat)
      
    def reverseEachRow(self,mat):
        for i in range(len(mat)):
            mat[i]=mat[i][::-1]
        
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)