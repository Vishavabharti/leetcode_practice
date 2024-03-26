class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        s = s.split(" ")
        if len(pattern) != len(s):
            return False

        hashmap = dict()
        used_words = set()

        for element in range(len(pattern)):
            char = pattern[element]
            word = s[element]
            if  char in hashmap:
                if hashmap[char] != word:
                    return False
            else:
                if word in used_words:
                    return False
                else:
                    hashmap[char] = word
                    used_words.add(word)
        
        return True


# Iterate over pattern length
# Set char and word and create empty hashmap 
# Check if "char" key: value "word" is not equal return false
# Else if word in used words return false
# Else set char key's value as word
# Append word in used word so that it will not used for another char
                
