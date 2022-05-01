

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
    def maximumWealth(self, accounts):
        
        temp = []
        for row in accounts:
            temp.append(sum(row))

        m = max(temp)
        
        return m

            
s = Solution();

accounts = [[1,2,3],[3,2,1]]
accounts = [[1,5],[7,3],[3,5]]
print(s.maximumWealth(accounts))
