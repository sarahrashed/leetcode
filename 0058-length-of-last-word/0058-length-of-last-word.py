class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        split_str = s.split()

        return len(split_str[len(split_str)-1])
