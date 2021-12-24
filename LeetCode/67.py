
class Solution:
    def addBinary(self, a, b):
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]


ob = Solution()
a = "11"
b = "1"
print(ob.addBinary(a, b))
