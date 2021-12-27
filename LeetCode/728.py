class Solution:
    def selfDividingNumbers(self, left, right):
        temp = []
        for i in range(left, right + 1):
            if self.another(i):
                temp.append(i)
        return temp

    def isDevided(self, n):
        for i in str(n):
            if i == '0' or n % int(i) > 0:
                return False
        return True

    def another(self, n):
        temp = n
        while temp != 0:
            rem = temp % 10
            if rem == 0 or n % rem != 0:
                return False
            temp = temp // 10
        return True


left = 1
right = 22

ob = Solution()
print(ob.selfDividingNumbers(left, right))
