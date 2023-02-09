
class Solution():
    def countDigits(self, num):
        t = []
        [t.append(int(i)) for i in str(num)]
        
        c = 0 
        for i in t:
            if num % i == 0: c += 1
        return c
    
        
        
        
s = Solution()
num = 1248
print(s.countDigits(num))