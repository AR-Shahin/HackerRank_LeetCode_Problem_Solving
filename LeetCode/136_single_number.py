class Solution:
    def singleNumber(self, nums):
        for n in nums:
            if nums.count(n) == 1:
                return n


ob = Solution()
nums = [4, 1, 2, 1, 2]
print(ob.singleNumber(nums))
