
class Solution():
    def smallerNumbersThanCurrent(self, nums):
        t = []
        
        for n in nums:
            c = 0
            for j in nums:
                if n > j:
                    c += 1
            t.append(c)   
           
                
        return t
        
        
        
s = Solution()
nums = [7,7,7,7]

print(s.smallerNumbersThanCurrent(nums))
