class Solution:
    def countOdds(self, low, high):
        count = 0
        for i in range(low, high + 1):
            if i % 2 != 0:
                count += 1
        return count


ob = Solution()
low = 3
high = 7
print(ob.countOdds(low, high))
# return (high + 1) // 2 - low // 2
