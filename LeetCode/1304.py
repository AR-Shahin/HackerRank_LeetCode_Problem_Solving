class Solution:
    def sumZero(self, n):
        temp = []
        mid = n // 2
        for i in range(1,mid +1):
            temp.append(-i)
            temp.append(i)
        if n % 2 != 0:
            temp.append(0)
        return temp
            
            
                    
s = Solution();

num1 = 3

print(s.sumZero(num1))
