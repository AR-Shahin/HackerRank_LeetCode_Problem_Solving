class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


ob = Solution()
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(ob.containsDuplicate(nums))
