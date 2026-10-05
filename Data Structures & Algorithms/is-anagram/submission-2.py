class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        for char in t:
            if hashmap.get(char, 0) == 0:
                return  False   # a letter in 't' was found, that is not in 's'
            hashmap[char] -= 1
                    
        return True






        if len(s) != len(t):
            return False

        hashmap = {}
        hashmap2 = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        for char in t:
            if hashmap.get(char, 0) == 0:
                return  False   # a letter in 't' was found, that is not in 's'
            hashmap[char] -= 1
            hashmap2[char] = hashmap2.get(char, 0) + 1
            
        for char in s:
            if hashmap[char] != hashmap2.get(char, 0):
                return False
        
        return True












        