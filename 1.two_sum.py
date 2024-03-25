class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = dict()
        
        # Iterate a nums array
        for index, element in enumerate(nums):
            diff = target - element
            if diff in hashmap:
                return [index, hashmap[diff]]
            else:
                hashmap[element] = index


# create a hashmap
# loop over the array
# get the element and its index
# computer the diff ie target - the value
# If the diff is in hashmap then return indexes else add the element to hashmap
