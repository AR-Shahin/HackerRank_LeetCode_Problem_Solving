
class Solution(object):
    def differenceOfSum(self, nums):

        temp = sum(nums)
        n = self.another(nums)
        s = 0
        while n != 0:
            r = n % 10
            s += r
            n = n // 10
        return abs(temp - s)
        
    def another(self,nums):
        sNum = [str(i) for i in nums]
        
        t =''
        for i in sNum:
            t += i
        
        return int(t)
        
s = Solution()
nums = [1,2,3,4]
print(s.differenceOfSum(nums))