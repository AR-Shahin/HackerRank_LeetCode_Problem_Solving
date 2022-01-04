class Solution:
    def addDigits(self, nums):
        l = len(str(nums))
        s = 0
        if nums >= 1 and nums <= 9:
            s = nums
        while l != 1:
            s = sum(list([int(x) for x in str(nums)]))
            l = len(str(s))
            nums = s
        return s


ob = Solution()
nums = 1
print(ob.addDigits(nums))

n = 111

print()
