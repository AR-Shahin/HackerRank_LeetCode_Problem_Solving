
class Solution(object):
    def getCommon(self, nums1, nums2):
        t = []
        for i in nums1:
            for j in nums2:
                if i == j: t.append(i)
        return min(t)
        
        
s = Solution()
nums1 = [1,2,3]
nums2 = [2,4]
print(s.getCommon(nums1,nums2))

class Solution(object):
    def getCommon(self, nums1, nums2):
        nums1, nums2 = set(nums1), set(nums2)
        common = sorted(list(nums1.intersection(nums2))) # sorted(list(nums1 & nums2))  will also work
        return -1 if not len(common) else common[0]
        
        
s = Solution()
nums1 = [1,2,3]
nums2 = [2,4]
print(s.getCommon(nums1,nums2))
