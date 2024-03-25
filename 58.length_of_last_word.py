class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        return len(s.split(" ")[-1])


# Strip the string to remove empty spaces
# Split the string will return the list of words
