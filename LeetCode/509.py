class Solution:
    def fib(self, n):
        first,second = 0,1
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return second
        if n > 2:
            for i in range(3,n+1):
                next = first + second
                if i == n:
                    return second + next
                first ,second = second,next
            
            
                    
s = Solution();

c = 3
print(s.fib(c))
