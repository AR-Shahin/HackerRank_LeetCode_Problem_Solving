class Solution:
    def maximumProduct(self, nums):
        sum = 1
        nums.sort(reverse=True)
        for i in nums[0:3]:
            sum *= i
        
        return sum    

    
s = Solution();

nums = [1,2,3,4]


print(s.maximumProduct(nums))
