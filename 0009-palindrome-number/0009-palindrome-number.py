import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:  # Negative numbers cannot be palindromes
            return False
            
        digits = [int(i) for i in str(x)]

        for i in range(int(math.floor(len(digits) / 2))):
            if digits[i] != digits[len(digits) - i - 1]:
                return False
        return True

        