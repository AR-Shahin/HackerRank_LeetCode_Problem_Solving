class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfDigit(n)
            
            if n == 1:
                return True
        
        return False
    
    def sumOfDigit(self,n):
        sum = 0
        
        while n:
            r = n % 10
            
            sum += r*r
            n = n //10
            
        return sum