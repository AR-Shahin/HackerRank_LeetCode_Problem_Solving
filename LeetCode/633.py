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
