class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = dict()
        
        # Iterate an nums array
        for index, element in enumerate(nums):
            diff = target - element
            if diff in hashmap:
                return [index, hashmap[diff]]
            else:
                hashmap[element] = index


# create a hashmap
# loop over the array
# get the element oand its index
# computer the complimnet ie target - the value
# if the diff is in hashmap then retun indexes else add the element to hashmap
