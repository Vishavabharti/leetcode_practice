class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap_s = dict()
        hashmap_t = dict()

        # Checks the lenght of the strings
        if len(s) != len(t):
            return False

        # Count of each char in s
        for char in s:
            if char in hashmap_s:
                hashmap_s[char] += 1
            else:
                hashmap_s[char] = 1

        # Count of each char in t
        for char in t:
            if char in hashmap_t:
                hashmap_t[char] += 1
            else:
                hashmap_t[char] = 1 

        # Checks the char count
        return hashmap_s == hashmap_t


        # First check the len of both the strings
        # Create empty hahsmap for both the strings
        # Check the count of letter in th each strings
        # If count of char matches then return True else False

        # soem other optimized solutions
        #-------------------------------------
        # for char in t:
        #     if char in hashmap.keys():
        #         if hashmap[char] == 1:
        #             del hashmap[char]
        #         else:
        #             hashmap[char] -=1
        #     else:
        #         return False

        # if len(hashmap) == 0:
        #     return True
        # else:
        #     return False
        #--------------------------------
        # for w in set(s):
        #     if s.count(w)!=t.count(w):
        #         return False
        # return True
        #----------------------------------
