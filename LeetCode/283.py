class Solution:
    def moveZeroes(self, nums):
        left = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        return nums


ob = Solution()
nums = [10, 1, 0, 3, 12]
print(ob.moveZeroes(nums))
