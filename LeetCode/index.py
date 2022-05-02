

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




from itertools import count


class Solution:
    def countEven(self, num):
        
        count = 0
       
        for n in range(1,num + 1):
            if sum([int(x) for x in str(n)]) % 2 == 0:
                count += 1
        
        return count

            
s = Solution();

num = 30
print(s.countEven(num))


