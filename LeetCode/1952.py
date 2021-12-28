class Solution:
    def isThree(self, n):
        k = 0
        for i in range(1, n+1):
            if n % i == 0:
                k += 1
        return True if k == 3 else False
