
class Solution:
    def diagonalSum(self, mat):
        
        l = len(mat[0])
        sum = 0
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                if i == j:
                    sum += mat[i][j]   
                    sum += mat[i][len(mat)-i-1]
                              
        if l % 2 != 0:
            sum = sum - mat[l//2][l//2]
        
        return sum

            
s = Solution();

mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]

print(s.diagonalSum(mat))

# mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]

# mat = [[5]]
