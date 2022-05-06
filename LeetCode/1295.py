class Solution:
    def findNumbers(self, nums):
        count = 0 
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
            
                    
s = Solution();

nums = [12,345,2,6,7896]
nums = [555,901,482,1771]
print(s.findNumbers(nums))
