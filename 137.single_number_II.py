class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashmap = dict()

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for element in hashmap:
            if hashmap[element] == 1:
                return element


# Create hashmap and add count of each array element
# Iterate hashmap return key where value is 1
