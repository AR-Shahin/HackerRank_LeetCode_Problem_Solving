class Solution:
    def singleNumber(self, nums):
        
        temp =  list(set(nums) )
        
        for i in temp:
            if nums.count(i) == 1:
                return i
            
            
                    
s = Solution();

nums = [0,1,0,1,0,1,99]

print(s.singleNumber(nums))
