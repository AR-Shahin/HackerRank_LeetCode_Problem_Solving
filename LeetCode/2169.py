class Solution:
    def countOperations(self, num1,num2):
        count = 0
        i = 1
        while num1 != 0 or num2 != 0:
           
            if num1 == 0 or num2 == 0:
                break
            elif num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            count +=1
        return count
            
            
                    
s = Solution();

num1 = 10
num2 = 10
print(s.countOperations(num1,num2))
