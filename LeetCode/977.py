class Solution:
    def sortedSquares(self, nums):
        temp = []
        for i in nums:
            temp.append(i*i)
        temp.sort()
        return temp
        return sorted(nums)


ob = Solution()
nums = [-4, -1, 0, 3, 10]
print(ob.sortedSquares(nums))
