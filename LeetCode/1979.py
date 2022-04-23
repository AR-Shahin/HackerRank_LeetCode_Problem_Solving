class Solution:
    def findGCD(self, nums):
        max_val = max(nums)
        min_val = min(nums)
        
        temp = []
        for i in range(1,min_val +1):
            if max_val % i == 0 and min_val % i == 0:
                temp.append(i)
        return max(temp)
        
        

s = Solution();

nums = [3,3]


print(s.findGCD(nums))
