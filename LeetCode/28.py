
# str = "my name is shahin"
# result = str.find('iss')
# print(result)


class Solution:
    def strStr(self, haystack, needle):
        index = haystack.find(needle)
        return index


ob = Solution()
haystack = ""
needle = ""
print(ob.strStr(haystack, needle))
