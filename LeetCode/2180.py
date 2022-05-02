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
