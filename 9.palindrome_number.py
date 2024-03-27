class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
    
        # Reverse the digits
        reversed_x = int(str(x)[::-1])
        #print(str(x)[:-1])
        
        # Compare the original and reversed integers
        return x == reversed_x
