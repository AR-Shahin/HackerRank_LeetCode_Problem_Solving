class Solution:
    def checkPerfectNumber(self, num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return True if sum == num else False


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        list = [6, 28, 496, 8128, 33550336]
        return (num in list)


ob = Solution()

print(ob.checkPerfectNumber(7))
