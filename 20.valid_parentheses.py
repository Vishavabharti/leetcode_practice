class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        valid = {")":"(", "}": "{", "]": "["}
        for element in s:
            if element in valid.values():
                stack.append(element)
            elif element in valid.keys():
                if not stack or valid[element] != stack.pop():
                    return False
            else:
              continue

        return not stack
