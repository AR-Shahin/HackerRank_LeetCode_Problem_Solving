class Solution:
    def searchInsert(self, nums, val):
        index = self.binary_search(nums, 0, len(nums), val)
        if index == -1:
            k = 0
            for i in range(len(nums)):
                if nums[i] < val:
                    k += 1
            return k
        else:
            return index

    def binary_search(self, A, low, high, val):
        if A[low] > val or A[high - 1] < val:
            return -1
        # if(low <= high):
        mid = (low + high) // 2

        if A[mid] == val:
            return mid
        elif A[mid] > val:
            return self.binary_search(A, low, mid-1, val)
        else:
            return self.binary_search(A, mid+1, high, val)


a = Solution()
nums = [1, 3, 5, 6]
print(a.searchInsert(nums, 7))
