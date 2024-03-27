class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase
        s = s.lower()
        
        # Remove non-alphanumeric characters
        clean_s = ''
        for char in s:
            if char.isalnum():
                clean_s += char
        
        # Check if the cleaned string is equal to its reverse
        return clean_s == clean_s[::-1]
