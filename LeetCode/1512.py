
class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        
        return count
        
        



s = Solution();

nums = [1,2,3]


print(s.numIdenticalPairs(nums))
