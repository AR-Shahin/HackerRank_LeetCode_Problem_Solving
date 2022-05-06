class Solution:
    def countPrimes(self, n):
        count = 0
        for i in range(2,n):
            if self.isPrime(i):
                # print(i)
                count += 1
        return count
    
    def isPrime(self,n):
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
            
                    
s = Solution();

nums = 3

print(s.countPrimes(nums))



class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
    
        primes = [False]*2 + [True]*(n-2)
        res = n - 2
        
        for i in range(2, math.ceil(math.sqrt(n))):
            if primes[i]:
                for j in range(i*i, n, i):
                    if primes[j]:
                        res -= 1
                        primes[j] = False
            
        return res
