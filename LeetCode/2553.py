
class Solution(object):
    def separateDigits(self, nums):
        t = []
        
        nums = [[t.append(j) for j in str(i)] for i in nums]
        
        return [int(i) for i in t]
        
        
s = Solution()
nums = [7,1,3,9]
print(s.separateDigits(nums))
