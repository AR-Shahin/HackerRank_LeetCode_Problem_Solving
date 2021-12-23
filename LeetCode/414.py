class Solution:
    def thirdMax(self, nums):
        nums = set(nums)
        # print(len(nums))
        if len(nums) < 3:
            return max(nums)

        else:
            i = 0
            temp = []
            while i != 3:
                m = max(nums)
                temp.append(m)
                nums.remove(m)
                i += 1
            return temp[-1]


ob = Solution()
nums = [3, 2, 1]
print(ob.thirdMax(nums))
