class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        for i in sorted(set(nums)):
            count = nums.count(i)
            if count > n / 2:
                return i


ob = Solution()
nums = [3, 2, 3]
print(ob.majorityElement(nums))
# a = (3)
# x = sorted(set(nums))
# print(x)
