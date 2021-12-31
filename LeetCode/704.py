class Solution:
    def search(self, nums: List[int], target: int) -> int:

        return self.binary_search(nums, 0, len(nums), target)

    def binary_search(self, nums, low, high, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low+((high-low) >> 1)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return -1
