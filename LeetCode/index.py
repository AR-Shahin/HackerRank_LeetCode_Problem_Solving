
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
# print(ob.largestOddNumber(nums))
print(nums[::-1])

# string = "Shahin"
# for c in string[::-1]:
#     print(c)


k = 0
while True:
    if 4**k + 6**k == 9**k:
        break
    else:
        k+=1
print(k)
