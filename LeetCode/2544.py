
class Solution(object):
    def alternateDigitSum(self, n):
        n = [int (i) for i in str(n)]
        t = 0
        for i in range(len(n)):
            if i % 2 == 0: t += n[i]
            else: t -= n[i]
        return t
        
        
s = Solution()
n = 521
print(s.alternateDigitSum(n))


