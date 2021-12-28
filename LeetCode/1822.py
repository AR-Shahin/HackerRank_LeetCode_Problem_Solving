class Solution:
    def arraySign(self, nums: List[int]) -> int:

        sum = 1
        for i in nums:
            sum *= i
        if sum > 0:
            return 1
        elif sum == 0:
            return 0
        else:
            return -1
