# # Bruteforce
# class Solution:
#     def isSameTree(self, p, q):
#         is_same = False
#         if len(p) == len(q):
#             for i in range(0, len(p)):
#                 if p[i] == q[i]:
#                     is_same = True
#                 else:
#                     is_same = False

#         return is_same


# ob = Solution()
# p = [1, 2]
# q = [1, None, 2]

# print(ob.isSameTree(p, q))







# first = 0
# second = 1

# n = 10
# if n == 1:
#     print(first)

# if n == 2:
#     print(first, second)

# if n > 2:
#     print(first)
#     print(second) 
#     for i in range(2,n):
#         res = first + second
#         print(res)
#         first = second
#         second = res

import math


# class Solution:
#     def largestPerimeter(self, nums):
#         nums.sort(reverse=True)
#         a,b,c = nums[0],nums[1],nums[2]
#         perimeter = sum([a,b,c])
#         half = perimeter / 2
        
#         area = math.sqrt(half * (half - a) * (half - b) * (half - c))
#         return perimeter if area != 0 else 0
         
    
    
    
    
    
    
# s = Solution();

# nums = [3,6,2,3]

# print(s.largestPerimeter(nums))

class Solution:
    def addToArrayForm(self, num, k):
        temp = ''.join(str(e) for e in num)
        sum = int(temp) + k
        converted_num = str(sum)
        
        return list(converted_num)
        
        



s = Solution();

num = [2,7,4]
k = 181

print(s.addToArrayForm(num,k))
