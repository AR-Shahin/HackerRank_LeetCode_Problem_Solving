
class Solution:
    def largestOddNumber(self, nums):
        if int(nums) % 2 != 0:
            return nums
        k = 0
        for c in nums[::-1]:
            if int(c) % 2 == 0:
                k += 1
            else:
                return nums[:-k]
        return ""


ob = Solution()
nums = "52113"
