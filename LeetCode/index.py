

# class Solution:
#     def checkStraightLine(self, coordinates):
        
#         for axis in range(0,len(coordinates)):
            
#            X = (coordinates[axis+1][1] - coordinates[axis][1]) * (coordinates[axis+1][0] - coordinates[axis][0])
           
#            Y = (coordinates[axis+2][1] - coordinates[axis + 1][1]) * (coordinates[axis+1][0] - coordinates[axis][0])
            
#            return True if X == Y else False

    
# s = Solution();

# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# # coordinates = [[0,0],[0,1],[0,-1]]

# print(s.checkStraightLine(coordinates))




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


# mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]

# mat = [[5]]
print(s.diagonalSum(mat))
