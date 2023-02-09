class Solution(object):
    def maximumCount(self, nums):
        t1,t2 = 0,0
        for i in nums:
            if i > 0:
                t1 += 1
            elif i < 0:
                t2 += 1
            
        return max([t1,t2])
        
s = Solution()
nums = [-3,-2,-1,0,0,1,2]
print(s.maximumCount(nums))
