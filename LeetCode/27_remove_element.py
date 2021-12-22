class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


a = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(a.removeElement(nums, 2))
