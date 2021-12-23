class Solution:
    def findDisappearedNumbers(self, nums):
        temp, nums = list(range(1, len(nums) + 1)), set(nums)
        return [i for i in temp if i not in nums]


ob = Solution()
nums = [1, 1]
print(ob.findDisappearedNumbers(nums))
