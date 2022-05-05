

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






# class Solution:
#     def isHappy(self, n):

#         while n != 1:
#             temp = [int(x) for x in str(n)]

#             n = sum([int(x) * int(x) for x in str(n)])
#             print(n)

#             return True if n == 1 else False


            
# s = Solution();

# n = 19
# print(s.isHappy(n))


from math import sqrt


class Solution:
    def judgeSquareSum(self, c):
        
        low, high = 0, int(sqrt(c))
        while low<=high:
            sum = low * low + high * high
            if sum == c:
                return True
            elif sum < c:
                low +=1
            else:
                high -=1
        return False
            
                    
s = Solution();

c = 3
print(s.judgeSquareSum(c))
# print(int(sqrt(c+1)))
