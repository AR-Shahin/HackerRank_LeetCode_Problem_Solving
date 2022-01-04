import math


class Solution:
    def constructRectangle(self, area):
        x = int(math.sqrt(area))

        while True:
            y = area / x
            if y.is_integer():
                if x > y:
                    return [x, int(y)]
                else:
                    return [int(y), x]
            x -= 1


ob = Solution()
nums = 200
print(ob.constructRectangle(nums))
