class Solution:
    def lengthOfLastWord(self, s):

        list = s.strip().split(" ")
        return len(list[-1])
